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


col1, col2 = st.columns(2)


col1.markdown('''##### A análise dos grandes números do e-commerce já nos revelou insights valiosos que podem direcionar nossas estratégias de marketing e vendas.
            
##### Observamos que os vinhos com preços de até R$99,00 são os campeões em geração de receita, destacando-se como os favoritos dos consumidores. Geograficamente, a região Sudeste lidera com folga em termos de geração de receita, seguida pelas regiões Centro-Oeste e Nordeste. ''')

col2.markdown(''' ##### Além disso, a idade dos consumidores se mostrou uma variável crucial para o nosso negócio. À medida que a faixa etária aumenta, observamos um aumento no consumo de vinho, indicando que consumidores mais velhos tendem a gastar mais em vinhos. Em relação aos tipos de vinho, o vinho tinto se destaca como o principal gerador de receita, sendo a preferência predominante entre os nossos clientes. ''')



st.divider()


st.markdown('''
##### Preferência da origem do vinho por Região em quantidade de pedidos :wine_glass:
- **Os vinhos de origem Europeia são os preferidos na maioria das regiões do Brasil**
''')

st.image("https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/imagens/pais_do_vinho_regiao.png", caption='Analisar a popularidade de vinhos de diferentes países por região do Brasil pode ajudar a otimizar o estoque e a criar campanhas. Além disso, podemos verificar a demanda por vinhos de países específicos e negociar melhores condições com fornecedores.', use_column_width=True)


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
