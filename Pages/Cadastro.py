import streamlit as st

st.sidebar.empty()

# Título da página de cadastro
st.title("Página de Cadastro")

# Campos de cadastro (nome, sobrenome, telefone, senha, confirmação de senha)
nome = st.text_input("Nome")
sobrenome = st.text_input("Sobrenome")
telefone = st.text_input("Número de telefone")
senha = st.text_input("Senha", type="password")
confirmar_senha = st.text_input("Confirmar senha", type="password")

# Botão para voltar à página de login
if st.button("Já tem cadastro? Voltar para login"):
    st.session_state.pagina = "Login"  # Redireciona de volta para a página de login

# Se houver dados do cadastro, você pode processar aqui...
