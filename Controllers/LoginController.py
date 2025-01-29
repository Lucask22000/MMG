import sqlite3

# Função para realizar o login de um cliente
def login_cliente(telefone, senha):
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clientes WHERE telefone = ? AND senha = ?", (telefone, senha))
    cliente = c.fetchone()
    conn.close()
    return cliente