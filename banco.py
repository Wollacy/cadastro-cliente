import sqlite3

# Criar banco de dados e tabela caso não existam
def criar_tabela():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            codigo TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """)
    conexao.commit()
    conexao.close()

