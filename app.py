import streamlit as st

#Cria a pagina de login
st.set_page_config(page_title="MM Montagem", page_icon="img.favicon.png")

# Título e img
st.markdown("<h1 style='text-align: center; color: DarkGray;'>Bem-vindo(a) à agenda MMG</h1>", unsafe_allow_html=True)

st.image("img\logo.png", width=700)

# Campo de usuario
def formatar_telefone(numero):
    numero = ''.join(filter(str.isdigit, numero))  # Remove caracteres não numéricos
    if len(numero) == 11:
        return f"({numero[:2]}) {numero[2:7]}-{numero[7:]}"
    elif len(numero) == 10:
        return f"({numero[:2]}) {numero[2:6]}-{numero[6:]}"
    return numero  # Retorna como está se não atender os critérios

telefone = st.text_input("Informe um número válido com DDD", placeholder="(99) 99999-9999")

telefone_formatado = formatar_telefone(telefone)

if telefone.strip():
    st.write(f"📞 Você digitou: {telefone_formatado}")

# Campo de senha
senha = st.text_input("Digite sua senha", type="password", placeholder="********", key="senha_login")

# Botão de login
if st.button("Entrar"):
    cliente = (telefone_formatado, senha)
    if cliente:
        st.success(f"Login realizado com sucesso para {cliente[0]}!")
    else:
        st.error("Número de telefone ou senha inválidos.")

# Botão de cadastro
if st.button("Não tem cadastro? Clique aqui para cadastrar"):
    st.session_state.pagina = "Cadastro"



