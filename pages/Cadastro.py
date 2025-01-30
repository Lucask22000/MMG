import streamlit as st

st.title("Cadastro de Usuário")

# Oculta completamente a barra lateral e o botão de expandir
st.markdown("""
    <style>
        [data-testid="stSidebar"], [data-testid="collapsedControl"] {
            display: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# Aqui você pode adicionar os campos do formulário de cadastro
nome = st.text_input("Nome")
sobrenome = st.text_input("Sobrenome")
telefone = st.text_input("Telefone")
senha = st.text_input("Senha", type="password")
confirmar_senha = st.text_input("Confirmar Senha", type="password")

if st.button("Cadastrar"):
    st.session_state["mensagem_sucesso"] = "Cadastro realizado com sucesso!"
    st.switch_page("app.py")  # Redireciona para a página inicial