import streamlit as st


# Configuração da página
st.set_page_config(page_title="Agenda MMG")

# Inicializa o estado da sessão para o telefone
if "telefone" not in st.session_state:
    st.session_state.telefone = ""

# Função para atualizar o estado do telefone
def atualizar_telefone():
    telefone = st.session_state.telefone
    st.session_state.telefone = formatar_telefone(telefone)

# Criando uma coluna centralizada
def centralizar_conteudo_streamlit(titulo, caminho_imagem, largura_imagem=320):
    col1, col2, col3 = st.columns([1, 4, 1])  # Cria colunas para centralizar
    with col2:
        st.subheader(titulo)  # Exibe o título
        st.image(caminho_imagem, width=largura_imagem)  # Exibe a imagem

# Exemplo de uso
centralizar_conteudo_streamlit("Bem-vindo(a) à agenda MMG", "imagens/mmg.jpg", largura_imagem=320)


st.write("""#### Agende agora mesmo uma data para que possamos entrar em contato com você""")

# Campo de entrada de telefone com formatação dinâmica
st.text_input(
    "Digite seu número de telefone",
    placeholder="(67) 99109-2895",
    key="telefone",
    on_change=atualizar_telefone
)

# Função para formatar o número no padrão nacional
def formatar_telefone(numero):
    # Remove caracteres não numéricos
    numero = ''.join(filter(str.isdigit, numero))
    
    # Aplica o formato (XX) XXXXX-XXXX para 11 dígitos
    if len(numero) == 11:
        return f"({numero[:2]}) {numero[2:7]}-{numero[7:]}"
    elif len(numero) == 10:  # Para números com 10 dígitos (sem o 9 extra)
        return f"({numero[:2]}) {numero[2:6]}-{numero[6:]}"
    return numero  # Retorna como está se não atender os critérios

# Campo de senha (ocultado)
senha = st.text_input("Digite sua senha", type="password", placeholder="********")

# Botão de login
if st.button("Entrar"):
    telefone = st.session_state.telefone
    if len(telefone) in [14, 15]:  # Verifica se está no formato correto
        st.success(f"Login realizado com o número {telefone}!")
    else:
        st.error("Por favor, insira um número válido no formato (XX) XXXXX-XXXX ou (XX) XXXX-XXXX.")
# Exibe a senha, mas você pode fazer validações ou outras ações com ela
if senha:
    st.write("Senha inserida.")

# Link para cadastro
st.write("Ainda não tem uma conta? [Cadastre-se aqui](#) para começar a agendar seus serviços!")

