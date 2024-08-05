from pathlib import Path
from datetime import date, timedelta

import plotly.express as px
import streamlit as st
import pandas as pd

from utilidades import leitura_de_dados


st.markdown(''' # Notas do Desenvolvimento 	:pencil:''')


st.divider()


st.markdown('''
Primeiramente, importei as duas tabelas no Python para analisar as bases de dados. 
Identifiquei as semelhanças e diferenças entre elas e segui a ordem indicada nas instruções do case para análise.
Decidi explorar primeiro a base de dados Vendas_Evino.xlsx, realizei o tratamento dos nomes das colunas e a análise descritiva inicial.
''')


url = "https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/bases/Vendas_Evino.csv"
df = pd.read_csv(url, sep=';', encoding='latin1')


df = df.loc[:, ~df.columns.str.contains('^Unnamed')]


df = df.head()
st.table(df)

st.markdown('''
Analisando as informações contidas na base, decidi que seria melhor gerar um cubo com alguns agrupamentos, 
como Região do Brasil para a coluna UF e faixa de idade para a coluna idade, facilitando a visualização e geração de insights. 
Para gerar o cubo, decidi usar SQL para demonstrar minhas habilidades em queries e na integração do Python com bancos de dados, 
algo crucial no ambiente corporativo onde frequentemente lidamos com dados provenientes de bancos de dados SQL.

Criei uma variável engine para armazenar as informações de conexão e usei a função to_sql para escrever o DataFrame. 
Em uma query SQL, criei as colunas de agrupamento por faixa etária (baseada na coluna idade) e por Região do Brasil 
(baseada na coluna UF). Também criei as colunas soma_receita, soma_pedidos e soma_clientes, agrupando pelas cinco primeiras colunas. ''')

url2 = "https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/bases/cubo_vendas.csv"
df2 = pd.read_csv(url2, sep=';', encoding='latin1')


df2 = df2.loc[:, ~df.columns.str.contains('^Unnamed')]


df2 = df2.head()
st.table(df)


