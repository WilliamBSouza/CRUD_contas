import sqlite3


# Criando o banco de dados
conexao = sqlite3.connect('contas.db')
cursor = conexao.cursor()

#criando as tabelas
"""
cursor.execute('''
    CREATE TABLE ContasAPagar (
        id INTEGER PRIMARY KEY,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        data_vencimento DATE NOT NULL,
        pago BOOLEAN NOT NULL
    )
''')

cursor.execute('''
CREATE TABLE ContasAReceber (
    id INTEGER PRIMARY KEY,
    descricao TEXT NOT NULL,
    valor REAL NOT NULL,
    data_A_Receber DATE NOT NULL,
    Recebido BOOLEAN NOT NULL
);
''')

"""

# Salvando as alterações e fechando a conexão
conexao.commit()
conexao.close()

