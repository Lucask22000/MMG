import streamlit as st
from Controllers.ClienteController import formatar_telefone
from Controllers.LoginController import login_cliente

if "logado" not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    st.markdown("""
        <style>
        [data-testid="stSidebar"] {display: none;}
        </style>
    """, unsafe_allow_html=True)

# Função de centralização de conteúdo
def centralizar_conteudo_streamlit(titulo, caminho_imagem, largura_imagem=320):
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.subheader(titulo)
        st.image(caminho_imagem, width=largura_imagem)

# Título e imagem
centralizar_conteudo_streamlit("Bem-vindo(a) à agenda MMG", "imagens/mmg.jpg", largura_imagem=320)

# Formulário de login
telefone_login = st.text_input("Digite seu número de telefone", placeholder="(67) 99109-2895", key="telefone_login")
senha = st.text_input("Digite sua senha", type="password", placeholder="********", key="senha_login")

if st.button("Entrar"):
    telefone_formatado = formatar_telefone(telefone_login)
    cliente = login_cliente(telefone_formatado, senha)
    if cliente:
        st.success(f"Login realizado com sucesso para {cliente[1]}!")
    else:
        st.error("Número de telefone ou senha inválidos.")

if st.button("Não tem cadastro? Clique aqui para cadastrar"):
    st.session_state.pagina = "Cadastro"  # Altera o estado da página para "Cadastro"



