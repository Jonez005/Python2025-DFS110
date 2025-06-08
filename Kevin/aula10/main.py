import streamlit as st
from db import produtos

st.set_page_config(
    page_title='Listagem de Produtos'
)

st.title('Listagem de produtos')
st.table(produtos)


ir_para_cadastro = st.button('Ir para o cadastro de produtos')

if ir_para_cadastro:
    st.switch_page('./pages/Cadastrar_Produto.py')