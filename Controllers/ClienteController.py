import sqlite3

# Função para criar o banco de dados e a tabela de clientes
def criar_banco():
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone TEXT,
        senha TEXT
    )
    ''')
    conn.commit()
    conn.close()

# Função para adicionar um novo cliente ao banco de dados
def cadastrar_cliente(nome, telefone, senha):
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("INSERT INTO clientes (nome, telefone, senha) VALUES (?, ?, ?)", (nome, telefone, senha))
    conn.commit()
    conn.close()

# Função para verificar se o cliente já está registrado
def verificar_cliente(telefone):
    conn = sqlite3.connect('clientes.db')
    c = conn.cursor()
    c.execute("SELECT * FROM clientes WHERE telefone = ?", (telefone,))
    cliente = c.fetchone()
    conn.close()
    return cliente

# Função para formatar o número de telefone
def formatar_telefone(numero):
    # Remove caracteres não numéricos
    numero = ''.join(filter(str.isdigit, numero))
    
    # Aplica o formato (XX) XXXXX-XXXX para 11 dígitos
    if len(numero) == 11:
        return f"({numero[:2]}) {numero[2:7]}-{numero[7:]}"
    elif len(numero) == 10:  # Para números com 10 dígitos (sem o 9 extra)
        return f"({numero[:2]}) {numero[2:6]}-{numero[6:]}"
    return numero  # Retorna como está se não atender os critérios
