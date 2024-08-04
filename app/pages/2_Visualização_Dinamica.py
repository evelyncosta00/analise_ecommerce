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

# Seleção dos índices pelo usuário
indices_selecionados = st.sidebar.multiselect('Selecione os índices', list(COLUNAS_ANALISE.keys()))

# Seleção das colunas pelo usuário
col_analises_exc = [c for c in list(COLUNAS_ANALISE.keys()) if c not in indices_selecionados]
colunas_selecionadas = st.sidebar.multiselect('Selecione as colunas', col_analises_exc)

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
        }
    )
    st.plotly_chart(fig)