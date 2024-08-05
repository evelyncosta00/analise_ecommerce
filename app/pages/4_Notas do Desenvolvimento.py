from pathlib import Path
from datetime import date, timedelta

import plotly.express as px
import streamlit as st
import pandas as pd

from utilidades import leitura_de_dados


st.markdown(''' # Notas do Desenvolvimento 	:pencil:''')


st.divider()
st.markdown('''
Nesta página, você encontrará uma descrição completa de todo o processo de desenvolvimento do projeto. 
Desde a importação e análise dos dados até a aplicação de modelos e a geração de insights. ''')

st.markdown('''
Primeiramente, importei as duas tabelas disponibilizadas no Python para analisar as bases de dados. 
Identifiquei as semelhanças e diferenças entre elas e optei por desenvolver a análise seguindo a ordem indicada nas instruções do case.
Sendo assim, para concluir a etapa **Manipulação e Visualização de dados**, comecei explorando a base de dados Vendas_Evino.xlsx, realizei o tratamento dos nomes das colunas e a análise descritiva inicial.
''''')


url = "https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/bases/Vendas_Evino.csv"
df = pd.read_csv(url, sep=';', encoding='latin1')


df = df.loc[:, ~df.columns.str.contains('^Unnamed')]


df = df.head()
st.table(df)

st.markdown('''
Analisando as informações contidas na base, concli que seria melhor gerar um cubo com alguns agrupamentos, 
como **Região do Brasil** para a coluna **UF** e **Faixa de idade** para a coluna **Idade**, facilitando a visualização e geração de insights. 
Para gerar o cubo, decidi utilizar SQL para demonstrar minhas habilidades em queries e na integração do Python com bancos de dados, 
algo crucial no ambiente corporativo onde frequentemente lidamos com dados provenientes de bancos de dados SQL.

Criei uma variável engine para armazenar as informações de conexão e usei a função to_sql para escrever o DataFrame. 
Em uma query SQL, criei as colunas de agrupamento por faixa etária (baseada na coluna idade) e por Região do Brasil 
(baseada na coluna UF). Também criei as colunas soma_receita, soma_pedidos e soma_clientes, agrupando pelas cinco primeiras colunas. 
''')

url2 = "https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/bases/cubo_vendas.csv"
df2 = pd.read_csv(url2, sep=';', encoding='latin1')


df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]


df2 = df2.head()
st.table(df2)

st.markdown('''
Depois, importei essa query para um DataFrame no Python e gerei um arquivo Excel para visualizar algumas tabelas dinâmicas.
Com essas tabelas dinâmicas, percebi que teria todos os principais insights de forma clara e simples. Decidi então construir
um código para gerar tabelas dinâmicas no Python e apresentá-las com a biblioteca de visualização Streamlit. Com as tabelas
dinâmicas geradas em Python e os gráficos da biblioteca Plotly, consegui visualizar com ainda mais facilidade os principais insights,
que estão descritos na página de **Visão Geral**. Essas tabelas e gráficos podem ser consultados na página de **Visualização Dinâmica Vendas**.
''')



st.markdown('''
Plotei todos os grandes números, analisei as combinações que faziam sentido e, após isso, decidi partir para a segunda etapa do case:
#### Desenvolvimento de Modelos Estatísticos de CRM, especificamente a clusterização.


st.divider()


Trouxe a base Vendas_Clientes_Evino.xlsx para o Python, examinei as colunas e o comportamento dos dados, verifiquei valores nulos e
outros aspectos da análise exploratória. Realizei o tratamento dos nomes das colunas e criei variáveis dummies para as colunas 
range_de_preco e tipo_de_vinho, transformando esses dados em categóricos para rodar o modelo K-means da biblioteca Scikit-learn, 
que é um algoritmo de clustering não supervisionado que organiza dados em K clusters, onde K é um número definido pelo usuário.
''')

st.markdown('''
##### Parâmetros usados na configuração do K-means:

- **n_clusters** = 10: Define o número de clusters (K) que você deseja formar.
- **max_iter** = 300: Número máximo de iterações do algoritmo K-means para uma única execução.
- **n_init** = 10: Número de vezes que o K-means será executado com diferentes centroides iniciais.
- **random_state** = 42: Define a semente do gerador de números aleatórios para garantir a reprodutibilidade dos resultados.

Com essas configurações, o K-means retornou 10 grupos numerados de 0 a 9. Escorei os clusters gerados ao DataFrame principal e 
decidi novamente gerar alguns agrupamentos no SQL. Escrevi o df em SQL e criei uma query para adicionar novas colunas de soma_garrafas,
soma_receita e count_qtd_clientes e agrupar pelas 3 primeiras colunas, o que resultou no cubo abaixo:
''')


url3 = "https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/bases/cubo_clientes_clusterizados.csv"
df3 = pd.read_csv(url3, sep=';', encoding='latin1')

df3 = df3.head()
st.table(df3)


st.markdown('''
Com esse cubo, pude visualizar novamente, através das tabelas dinâmicas do Excel, pude identificar os comportamentos que caracterizam os perfis 
de compra de cada cluster definido pelo algoritmo. Esses perfis foram descritos na página **Visão Geral** e as tabelas dinâmicas que 
me ajudaram a identificar cada perfil podem ser consultadas na página **Visualização Dinâmica Clusters**.
''')


st.divider()


st.markdown('''
Com este case, pude demonstrar algumas das minhas habilidades técnicas e analíticas. Espero ter mais desafios para criar cada vez mais 
soluções inteligentes baseadas em dados. :bar_chart:
''')

