import streamlit as st


# Configuração da página com o favicon
st.set_page_config(
    page_title="Agenda MMG",
    page_icon="imagens/favicon.png",  # Caminho do arquivo do favicon
    layout="centered"
)

# Verifica se o estado da página está definido, caso contrário, inicializa com a página de login
if "pagina" not in st.session_state:
    st.session_state.pagina = "Login"

# Usando a variável st.session_state.pagina para controlar a navegação
if st.session_state.pagina == "Login":
    import Pages.Login  # Importando a página de login
elif st.session_state.pagina == "Cadastro":
    import Pages.Cadastro  # Importando a página de cadastro
elif st.session_state.pagina == "Home":
    import Pages.Home  # Importando a página home
