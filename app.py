import streamlit as st

#Cria a pagina de login
st.set_page_config(page_title="MM Montagem", page_icon="img.favicon.png")

# Função de centralização de conteúdo
def centralizar_conteudo_streamlit(caminho_img, largura_img=320):
    col1, col2, col3 = st.columns([3, 3, 3])
    with col2:
        st.image(caminho_img, width=largura_img)

# Título e img
st.title("Bem-vindo(a) à agenda MMG")
centralizar_conteudo_streamlit("img/mmg.jpg", largura_img=320)

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



