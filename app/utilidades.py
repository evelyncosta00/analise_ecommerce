import streamlit as st
import pandas as pd

def leitura_de_dados():
    if 'dados' not in st.session_state:
        st.session_state['dados'] = {}

    if 'df_vendas' not in st.session_state['dados']:
        url = "https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/bases/cubo_vendas.csv"
        df_vendas = pd.read_csv(url, sep=';', decimal=',', thousands='.', encoding='latin1')

        # Converter todas as colunas numéricas para inteiros
        for col in df_vendas.select_dtypes(include=['float', 'int']).columns:
            df_vendas[col] = pd.to_numeric(df_vendas[col], downcast='integer')

        st.session_state['dados']['df_vendas'] = df_vendas

    if 'df_clientes' not in st.session_state['dados']:
        url = "https://raw.githubusercontent.com/evelyncosta00/analise_ecommerce/main/bases/cubo_clientes_clusterizados.csv"
        df_clientes = pd.read_csv(url, sep=';', decimal=',', thousands='.', encoding='latin1')

        # Converter todas as colunas numéricas para inteiros
        for col in df_clientes.select_dtypes(include=['float', 'int']).columns:
            df_clientes[col] = pd.to_numeric(df_clientes[col], downcast='integer')

        st.session_state['dados']['df_clientes'] = df_clientes
