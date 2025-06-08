import streamlit as st
from db import produtos


st.title('Gerenciamento de produtos')


with st.form('cadastras - produto ') as form:
    nome = st.text_input('nome', placeholder='Placa de video RTX 3070 ')
    preco = st.number_input('Preço')
    Quantidade = st.number_input('Quantidade', step=1)
    Categoria = st.selectbox(
        'Categoria',
    placeholder='selecione um opçao',
    index=None,
    options=['Alimentos', 'Higiene', 'Games', 'Eletronicos', 'Armarios de cozinha',]
    )


    button = st.form_submit_button('Cadastrar')

    if button:
        produto = {
            'nome': nome,
            'preco': preco,
            'Quantidade': Quantidade,
            'Categoria': Categoria
        }

        produtos.append(produto)

        st.table(produtos)