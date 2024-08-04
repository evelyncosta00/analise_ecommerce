from pathlib import Path
from datetime import date, timedelta

import plotly.express as px
import streamlit as st
import pandas as pd

from utilidades import leitura_de_dados



st.markdown(''' # Principais Insigths ''')


st.divider()


st.markdown(''' ### Vamos começar visualizando os grupos que mais geram receita. :bar_chart: ''')


st.divider()


st.markdown(''' 
#### Clusters de preços que geram maior receita no Ecommerce :moneybag:                         
- **Os vinhos de até R$99,00 são os campeões em geração de receita!**
''')
st.image("https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/imagens/receita_faixa_de_preco.png", use_column_width=True)



st.divider()



st.markdown('''
#### Regiões que geram mais receitas no Ecommerce :moneybag:
- **A região Sudeste lidera em geração de receita com folga, em seguida temos as regiões Centro-Oeste e Nordeste, também com receitas bem altas.**
''')
st.image("https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/imagens/receita_por_regiao.png", use_column_width=True)



st.divider()



st.markdown('''
#### Faixas de idade que geram mais receitas no Ecommerce :moneybag:
- **Podemos notar que a idade é uma variável importante para o nosso negócio, pois quanto maior a idade, maior o consumo de vinho, conforme observado no gráfico de receita por faixa etária.**
''')
st.image("https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/imagens/receita_por_faixa_etaria.png", use_column_width=True)




st.divider()



st.markdown('''
#### Tipos de Vinho que geram mais receitas no Ecommerce :moneybag:
- **O Vinho tinto é disparado o que mais gera receita para o nosso negócio!**
''')
st.image("https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/imagens/receita_tipo_vinho.png", use_column_width=True)



st.divider()



st.markdown('''
##### A análise dos grandes números do e-commerce já nos revelou insights valiosos que podem direcionar nossas estratégias de marketing e vendas.
            
##### Observamos que os vinhos com preços de até R$99,00 são os campeões em geração de receita, destacando-se como os favoritos dos consumidores. Geograficamente, a região Sudeste lidera com folga em termos de geração de receita, seguida pelas regiões Centro-Oeste e Nordeste.
##### Além disso, a idade dos consumidores se mostrou uma variável crucial para o nosso negócio. À medida que a faixa etária aumenta, observamos um aumento no consumo de vinho, indicando que consumidores mais velhos tendem a gastar mais em vinhos. Em relação aos tipos de vinho, o vinho tinto se destaca como o principal gerador de receita, sendo a preferência predominante entre os nossos clientes.
''')



st.divider()


st.markdown(''' ## Vamos agora analisar o Ecommerce em uma ótica combinada! ''')


st.divider()


st.markdown('''
##### Preferência da origem do vinho por Região em quantidade de pedidos :wine_glass:
- **Os vinhos de origem Europeia são os preferidos na maioria das regiões do Brasil**
''')

st.image("https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/imagens/pais_do_vinho_regiao.png", caption='Analisar a popularidade de vinhos de diferentes países por região do Brasil pode ajudar a otimizar o estoque e a criar campanhas. Além disso, podemos verificar a demanda por vinhos de países específicos e negociar melhores condições com fornecedores.', use_column_width=True)

