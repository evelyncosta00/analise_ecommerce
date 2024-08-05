import streamlit as st
import pandas as pd
import plotly.express as px
from utilidades import leitura_de_dados

# Definição das colunas de análise e valor
COLUNAS_ANALISE = {
    'Tipo do Vinho': 'tipo_do_vinho', 
    'País do Vinho': 'pais_do_vinho', 
    'Região': 'REGIAO', 
    'Faixa de Idade': 'faixa_etaria', 
    'Faixa de Preço do Vinho': 'cluster_de_preco_do_vinho'
}

COLUNAS_VALOR = {
    'Receita': 'SOMA_RECEITA', 
    'Pedidos': 'SOMA_PEDIDOS', 
    'Clientes': 'SOMA_CLIENTES'
}

FUNCOES_AGG = {
    'Soma': 'sum'
}

# Leitura dos dados
leitura_de_dados()
df_vendas = st.session_state['dados']['df_vendas']

# Definir o mapeamento para renomear os valores da coluna
mapeamento_preco = {
    "R$0 a R$49,99": "1-R$0 a R$49,99",
    "R$50 a R$99,99": "2-R$50 a R$99,99",
    "R$100 a R$199,99": "3-R$100 a R$199,99",
    "R$200 a R$399,99": "4-R$200 a R$399,99",
    "R$400 ou mais": "5-R$400 ou mais"
}

# Aplicar o mapeamento à coluna 'cluster_de_preco_do_vinho'
df_vendas['cluster_de_preco_do_vinho'] = df_vendas['cluster_de_preco_do_vinho'].replace(mapeamento_preco)

# Definir a ordem desejada para 'cluster_de_preco_do_vinho'
ordem_preco = list(mapeamento_preco.values())

# Aplicar a categoria ordenada à coluna 'cluster_de_preco_do_vinho'
df_vendas['cluster_de_preco_do_vinho'] = pd.Categorical(df_vendas['cluster_de_preco_do_vinho'], categories=ordem_preco, ordered=True)

# Inicialização da seleção de índices com 'Tipo do Vinho'
indices_iniciais = ['Tipo do Vinho']

# Seleção dos índices pelo usuário
indices_selecionados = st.sidebar.multiselect('Selecione apenas um índice por análise', list(COLUNAS_ANALISE.keys()), default=indices_iniciais)

# Seleção das colunas pelo usuário
col_analises_exc = [c for c in list(COLUNAS_ANALISE.keys()) if c not in indices_selecionados]
colunas_selecionadas = st.sidebar.multiselect('Selecione apenas uma coluna por análise', col_analises_exc)

# Seleção da coluna de valor pelo usuário
valor_selecionado = st.sidebar.selectbox('Selecione o valor de análise:', list(COLUNAS_VALOR.keys()))

# Seleção da métrica pelo usuário
metrica_selecionada = st.sidebar.selectbox('Selecione a métrica:', list(FUNCOES_AGG.keys()))

# Verificação das seleções e criação da tabela dinâmica
if len(indices_selecionados) > 0:
    metrica_selecionada = FUNCOES_AGG[metrica_selecionada]
    
    # Garantir que as colunas são unidimensionais
    for col in indices_selecionados + colunas_selecionadas:
        df_vendas[COLUNAS_ANALISE[col]] = df_vendas[COLUNAS_ANALISE[col]].astype(str)
    
    vendas_pivotadas = pd.pivot_table(
        df_vendas, 
        index=[COLUNAS_ANALISE[col] for col in indices_selecionados],
        columns=[COLUNAS_ANALISE[col] for col in colunas_selecionadas] if colunas_selecionadas else None,
        values=COLUNAS_VALOR[valor_selecionado],
        aggfunc=metrica_selecionada
    )

    # Adicionar coluna de total geral para ordenação
    vendas_pivotadas['TOTAL GERAL'] = vendas_pivotadas.sum(axis=1)

    # Ordenar a tabela dinâmica pelo total geral em ordem decrescente
    vendas_pivotadas = vendas_pivotadas.sort_values(by='TOTAL GERAL', ascending=False)

    # Remover "TOTAL GERAL" antes de exibir a tabela e criar o gráfico
    vendas_pivotadas = vendas_pivotadas.drop(columns='TOTAL GERAL', errors='ignore')

    # Criar uma cópia formatada para exibição na tabela
    vendas_pivotadas_formatada = vendas_pivotadas.applymap(lambda x: f"{int(x):,}".replace(",", ".") if pd.notnull(x) else "")

    st.dataframe(vendas_pivotadas_formatada)

    # Criar gráfico de barras
    vendas_pivotadas_reset = vendas_pivotadas.reset_index()

    # Garantir que todas as colunas especificadas em id_vars estejam presentes no DataFrame
    id_vars = [COLUNAS_ANALISE[col] for col in indices_selecionados]
    for col in id_vars:
        if col not in vendas_pivotadas_reset.columns:
            vendas_pivotadas_reset[col] = None  # Adiciona a coluna com valores padrão

    vendas_pivotadas_melt = vendas_pivotadas_reset.melt(
        id_vars=id_vars, 
        var_name='Categoria', 
        value_name='Valor'
    )

    # Ordenar os dados do gráfico pelo valor em ordem crescente
    vendas_pivotadas_melt = vendas_pivotadas_melt.sort_values(by='Valor', ascending=True)

    # Usar o nome da coluna real no DataFrame para a cor
    color_column = COLUNAS_ANALISE[indices_selecionados[0]]
    color_column_name = indices_selecionados[0]

    fig = px.bar(
        vendas_pivotadas_melt, 
        x='Categoria', 
        y='Valor', 
        color=color_column, 
        barmode='group',
        labels={
            'Categoria': 'Categoria',
            'Valor': valor_selecionado,
            color_column: color_column_name
        },
        category_orders={'Categoria': ordem_preco}  # Definir a ordem das categorias
    )
    st.plotly_chart(fig)
