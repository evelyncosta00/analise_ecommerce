import streamlit as st
import pandas as pd
import plotly.express as px
from utilidades import leitura_de_dados

# Definição das colunas de análise e valor para o novo DataFrame
COLUNAS_ANALISE_NOVO = {
    'Faixa de Preço': 'range_de_preco', 
    'Tipo de Vinho': 'tipo_de_vinho', 
    'Cluster': 'cluster'
}

COLUNAS_VALOR_NOVO = {
    'Receita': 'SOMA_RECEITA', 
    'Garrafas': 'SOMA_GARRAFAS', 
    'Clientes': 'QTD_CLIENTES'
}

FUNCOES_AGG = {
    'Soma': 'sum'
}

# Leitura dos dados
leitura_de_dados()
df_clientes = st.session_state['dados']['df_clientes']

# Definir o mapeamento para renomear os valores da coluna
mapeamento_preco = {
    "R$0 a R$49,99": "1-R$0 a R$49,99",
    "R$50 a R$99,99": "2-R$50 a R$99,99",
    "R$100 a R$199,99": "3-R$100 a R$199,99",
    "R$200 a R$399,99": "4-R$200 a R$399,99",
    "R$400 ou mais": "5-R$400 ou mais"
}

# Aplicar o mapeamento à coluna 'range_de_preco'
df_clientes['range_de_preco'] = df_clientes['range_de_preco'].replace(mapeamento_preco)

# Definir a ordem desejada para 'range_de_preco'
ordem_preco = list(mapeamento_preco.values())

# Aplicar a categoria ordenada à coluna 'range_de_preco'
df_clientes['range_de_preco'] = pd.Categorical(df_clientes['range_de_preco'], categories=ordem_preco, ordered=True)

# Seleção dos índices pelo usuário, com "Cluster" como padrão
indices_selecionados = st.sidebar.multiselect('Não altere esse índice', list(COLUNAS_ANALISE_NOVO.keys()), default=['Cluster'])

# Seleção das colunas pelo usuário
col_analises_exc = [c for c in list(COLUNAS_ANALISE_NOVO.keys()) if c not in indices_selecionados]
colunas_selecionadas = st.sidebar.multiselect('Selecione apenas uma coluna', col_analises_exc)

# Seleção da coluna de valor pelo usuário
valor_selecionado = st.sidebar.selectbox('Selecione o valor de análise:', list(COLUNAS_VALOR_NOVO.keys()))

# Seleção da métrica pelo usuário
metrica_selecionada = st.sidebar.selectbox('Selecione a métrica:', list(FUNCOES_AGG.keys()))

# Verificação das seleções e criação da tabela dinâmica
if len(indices_selecionados) > 0:
    metrica_selecionada = FUNCOES_AGG[metrica_selecionada]
    
    # Garantir que as colunas são unidimensionais
    for col in indices_selecionados + colunas_selecionadas:
        df_clientes[COLUNAS_ANALISE_NOVO[col]] = df_clientes[COLUNAS_ANALISE_NOVO[col]].astype(str)
    
    if len(colunas_selecionadas) == 0:
        # Calcular a soma total geral
        total_geral = df_clientes[COLUNAS_VALOR_NOVO[valor_selecionado]].sum()
        
        # Calcular o percentual do total geral
        df_clientes['percentual'] = df_clientes[COLUNAS_VALOR_NOVO[valor_selecionado]] / total_geral * 100
    else:
        # Calcular a soma total por cluster
        total_por_cluster = df_clientes.groupby('cluster')[COLUNAS_VALOR_NOVO[valor_selecionado]].transform('sum')
        
        # Calcular o percentual
        df_clientes['percentual'] = df_clientes[COLUNAS_VALOR_NOVO[valor_selecionado]] / total_por_cluster * 100
    
    vendas_pivotadas = pd.pivot_table(
        df_clientes, 
        index=[COLUNAS_ANALISE_NOVO[col] for col in indices_selecionados],
        columns=[COLUNAS_ANALISE_NOVO[col] for col in colunas_selecionadas] if colunas_selecionadas else None,
        values='percentual',
        aggfunc=metrica_selecionada
    )

    # Ordenar a tabela dinâmica pelo valor do índice selecionado em ordem crescente
    vendas_pivotadas = vendas_pivotadas.sort_index(ascending=True)

    # Criar uma cópia formatada para exibição na tabela
    vendas_pivotadas_formatada = vendas_pivotadas.applymap(lambda x: f"{x:.2f}%" if pd.notnull(x) else "")

    col1.markdown(''' 
    #### Selecione os campos para visualizar a tabela dinâmica             
    ''')
    st.dataframe(vendas_pivotadas_formatada)

    # Criar gráfico de barras
    vendas_pivotadas_reset = vendas_pivotadas.reset_index()

    # Garantir que todas as colunas especificadas em id_vars estejam presentes no DataFrame
    id_vars = [COLUNAS_ANALISE_NOVO[col] for col in indices_selecionados]
    for col in id_vars:
        if col not in vendas_pivotadas_reset.columns:
            vendas_pivotadas_reset[col] = None  # Adiciona a coluna com valores padrão

    vendas_pivotadas_melt = vendas_pivotadas_reset.melt(
        id_vars=id_vars, 
        var_name='Categoria', 
        value_name='Valor'
    )

    # Ordenar os dados do gráfico pelo valor do índice selecionado em ordem crescente
    vendas_pivotadas_melt = vendas_pivotadas_melt.sort_values(by=id_vars, ascending=True)

    # Usar o nome da coluna real no DataFrame para a cor
    color_column = COLUNAS_ANALISE_NOVO[indices_selecionados[0]]
    color_column_name = indices_selecionados[0]

    fig = px.bar(
        vendas_pivotadas_melt, 
        x='Categoria', 
        y='Valor', 
        color=color_column, 
        barmode='group',
        labels={
            'Categoria': 'Categoria',
            'Valor': 'Percentual',
            color_column: color_column_name
        },
        category_orders={'Categoria': ordem_preco}  # Definir a ordem das categorias
    )
    st.plotly_chart(fig)


st.divider()


st.markdown('''
## Clusters :jigsaw:            
''')

st.divider()


col1, col2 = st.columns(2)


col1.markdown(''' 
### Descomplicados :wine_glass:
**Apreciadores de vinhos tintos e rosé acessíveis.**

- **Faixa de Preço**: 0 a 49
- **Tipo de Vinho Predominante**: Tinto e Rosé
- **Clusters**: 2 e 7
              
- Preferem vinhos tintos e rosé na faixa de preço mais baixa.
- Optam por opções econômicas para consumo diário ou eventos informais.              
''')

col2.markdown(''' 
### Moderados :label:
**Apreciadores de vinhos tintos e rosé moderados.**

- **Faixa de Preço**: 50 a 99
- **Tipo de Vinho Predominante**: Tinto e Rosé
- **Clusters**: 1 e 8              

- Preferem vinhos tintos e rosé na faixa de preço média.
- Buscam um equilíbrio entre qualidade e custo, adequados para jantares e eventos sociais.             
''')

st.divider()



col1, col2 = st.columns(2)


col1.markdown(''' 
### Top Custo-Benefício: :gem:
**Apreciadores de vinhos brancos de bom custo benefício.**

- **Faixa de Preço**: 0 a 99
- **Tipo de Vinho Predominante**: Branco
- **Cluster**: 0
              
- Preferem vinhos brancos que variam entre preços baixos e médios, indicados para diferentes tipos de ocasiões.
- Buscam opções que ofereçam uma boa relação custo-benefício, tanto para consumo diário quanto para eventos mais formais.     
''')

col2.markdown(''' 
### Efervescentes: :clinking_glasses:
**Entusiastas de espumantes acessíveis**

- **Faixa de Preço**: 0 a 200
- **Tipo de Vinho Predominante**: Espumantes
- **Cluster**: 5           

- Preferem espumantes que variam de preços baixos a moderados.
- Buscam boas opções para celebrações e eventos sociais sem gastar muito.         
''')



st.divider()



col1, col2 = st.columns(2)


col1.markdown(''' 
### Premium: :star2:
**Amantes de vinhos Premium.**

- **Faixa de Preço**: Acima de 400
- **Tipo de Vinho Predominante**: Tinto, seguido por Rosé e Branco
- **Cluster**: 4
              
- Preferem vinhos de alta gama, com concentração em vinhos tintos e uma presença significativa de rosé e branco.
- Buscam vinhos de alta qualidade e estão dispostos a investir em opções premium para ocasiões especiais ou para colecionar.     
''')

col2.markdown(''' 
### Sofisticados: :tophat:
**Apreciadores de vinhos sofisticados**

- **Faixa de Preço**: 200 a 400
- **Tipo de Vinho Predominante**: Tinto, seguido por Rosé e Branco
- **Cluster**: 6           

- Preferem vinhos com um bom equilíbrio entre qualidade e preço, com maior concentração em tintos, mas também compram rosé e branco.
- Buscam vinhos que ofereçam sofisticação e valor para ocasiões especiais.
''')


st.divider()



col1, col2 = st.columns(2)


col1.markdown(''' 
### Top Valor: :medal:
**Amantes de vinhos de boa relação custo-benefício.**

- **Faixa de Preço**: 100 a 200
- **Tipo de Vinho Predominante**: Tinto, seguido por Rosé e Branco
- **Cluster**: 3
              
- Preferem vinhos que oferecem uma boa relação entre qualidade e preço, com maior ênfase em tintos, mas também compram rosé e branco.
- Buscam opções que combinam qualidade e acessibilidade, ideais para ocasiões variadas e eventos sociais.
''')

col2.markdown(''' 
### Exploradores: :earth_americas:
**Exploradores de Vinhos Variados**

- **Faixa de Preço**: 0 a 100
- **Tipo de Vinho Predominante**:  Leve concentração em Tinto, mas inclui Rosé e Branco
- **Cluster**: 9          

- Preferem explorar diferentes tipos de vinhos dentro de uma faixa de preço acessível.
- Buscam variedade e boas ofertas, experimentando várias opções de vinhos sem gastar muito.
''')
