from pathlib import Path
from datetime import date, timedelta

import plotly.express as px
import streamlit as st
import pandas as pd

from utilidades import leitura_de_dados

# Título do aplicativo
st.markdown(''' # Notas do Desenvolvimento 	:pencil:''')

# Divisor
st.divider()

# Descrição inicial
st.markdown('''
Primeiramente, importei as duas tabelas no Python para analisar as bases de dados. 
Identifiquei as semelhanças e diferenças entre elas e segui a ordem indicada nas instruções do case para análise.
Decidi explorar primeiro a base de dados Vendas_Evino.xlsx, realizei o tratamento dos nomes das colunas e a análise descritiva inicial.
''')

# Carregar o CSV em um DataFrame
url = "https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/bases/Vendas_Evino.csv"
df = pd.read_csv(url, sep=';', encoding='latin1')

# Remover colunas 'Unnamed'
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# Exibir as primeiras linhas do DataFrame
df = df.head()
st.table(df)
