import streamlit as st

if st.session_state.logado:
    st.sidebar.title("Menu")
    st.sidebar.write("Opções do Painel")
    # Adicione links para as páginas do painel aqui
else:
    # Não exibe opções ou links adicionais
    st.sidebar.write("Navegue para login ou cadastro.")

# Exemplo de página home
st.title("Página Inicial")
st.write("Aqui você pode gerenciar sua agenda e outras funcionalidades.")
