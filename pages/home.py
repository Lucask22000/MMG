import streamlit as st
import os

# Desativa a navegação automática, removendo o menu de páginas
st.set_page_config(initial_sidebar_state="collapsed", page_title="Minha Página")

st.title("Home")

st.success(f"Login realizado com sucesso!")