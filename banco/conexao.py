import sqlite3


def conectar():
    conexao = sqlite3.connect("dados/veiculos.db")
    return conexao


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS veiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            modelo TEXT NOT NULL,
            ano INTEGER NOT NULL,
            placa TEXT NOT NULL
        )
    """)

    # Adiciona as novas colunas caso ainda não existam
    cursor.execute("PRAGMA table_info(veiculos)")
    colunas = cursor.fetchall()

    nomes_colunas = [coluna[1] for coluna in colunas]

    if "pressao_dianteira" not in nomes_colunas:
        cursor.execute("""
            ALTER TABLE veiculos
            ADD COLUMN pressao_dianteira REAL
        """)

    if "pressao_traseira" not in nomes_colunas:
        cursor.execute("""
            ALTER TABLE veiculos
            ADD COLUMN pressao_traseira REAL
        """)

    conexao.commit()
    conexao.close()

