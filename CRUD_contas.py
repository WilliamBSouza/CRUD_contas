import sqlite3

# Conectando ao banco de dados e criando as tabelas
conexao = sqlite3.connect('contas.db')
cursor = conexao.cursor()
"""
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ContasAPagar (
        id INTEGER PRIMARY KEY,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        data_vencimento DATE NOT NULL,
        pago BOOLEAN NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS ContasAReceber (
        id INTEGER PRIMARY KEY,
        descricao TEXT NOT NULL,
        valor REAL NOT NULL,
        data_A_Receber DATE NOT NULL,
        Recebido BOOLEAN NOT NULL
    )
''')

conexao.commit()
"""
# Função para criar uma conta a pagar
def criar_conta_a_pagar():
    descricao = input("Qual a descrição da conta a pagar? ")
    valor = float(input("Qual o valor da conta a pagar? "))
    data_vencimento = input("Qual a data de vencimento da conta a pagar? ")
    pago = input("A conta já foi paga? (Sim/Não) ")

    cursor.execute('''
        INSERT INTO ContasAPagar (descricao, valor, data_vencimento, pago)
        VALUES (?, ?, ?, ?)
    ''', (descricao, valor, data_vencimento, pago))
    conexao.commit()

# Função para criar uma conta a receber
def criar_conta_a_receber():
    descricao = input("Qual a descrição da conta a receber? ")
    valor = float(input("Qual o valor da conta a receber? "))
    data_a_receber = input("Qual a data de vencimento da conta a receber? ")
    recebido = input("Quanto já foi recebido desta conta? ")
    
    cursor.execute('''
        INSERT INTO ContasAReceber (descricao, valor, data_A_Receber, Recebido)
        VALUES (?, ?, ?, ?)
    ''', (descricao, valor, data_a_receber, recebido))
    conexao.commit()


# Função para buscar todas as contas a pagar
def buscar_contas_a_pagar():
    cursor.execute('SELECT * FROM ContasAPagar')
    return cursor.fetchall()

# Função para buscar todas as contas a receber
def buscar_contas_a_receber():
    cursor.execute('SELECT * FROM ContasAReceber')
    return cursor.fetchall()


# Função para editar uma conta a pagar
def editar_conta_a_pagar(id_conta):
    descricao = input("Nova descrição da conta a pagar: ")
    valor = float(input("Novo valor da conta a pagar: "))
    data_vencimento = input("Nova data de vencimento da conta a pagar: ")
    pago = input("A conta já foi paga? (Sim/Não): ")

    cursor.execute('''
        UPDATE ContasAPagar
        SET descricao = ?, valor = ?, data_vencimento = ?, pago = ?
        WHERE id = ?
    ''', (descricao, valor, data_vencimento, pago, id_conta))
    conexao.commit()

# Função para editar uma conta a receber
def editar_conta_a_receber(id_conta):
    descricao = input("Nova descrição da conta a receber: ")
    valor = float(input("Novo valor da conta a receber: "))
    data_a_receber = input("Nova data de vencimento da conta a receber: ")
    recebido = input("Quanto já foi recebido desta conta? ")

    cursor.execute('''
        UPDATE ContasAReceber
        SET descricao = ?, valor = ?, data_A_Receber = ?, Recebido = ?
        WHERE id = ?
    ''', (descricao, valor, data_a_receber, recebido, id_conta))
    conexao.commit()

# Função para deletar uma conta a pagar
def deletar_conta_a_pagar(id_conta):
    cursor.execute('''
        DELETE FROM ContasAPagar
        WHERE id = ?
    ''', (id_conta,))
    conexao.commit()

# Função para deletar uma conta a receber
def deletar_conta_a_receber(id_conta):
    cursor.execute('''
        DELETE FROM ContasAReceber
        WHERE id = ?
    ''', (id_conta,))
    conexao.commit()



while True:
    menu = input("""Qual opção deseja realizar?
                [1] Adicionar conta a pagar
                [2] Adicionar conta a Receber
                [3] Editar conta a pagar
                [4] Editar conta a receber
                [5] Visualizar conta a pagar
                [6] Visualizar conta a receber
                [7] Deletar contas a pagar
                [8] Deletar contas a receber
                [9] Sair
                
                Opção: """)

    if menu == "1":
        criar_conta_a_pagar()

    elif menu == "2":
        criar_conta_a_receber()

    elif menu == "3":
        id_conta = int(input("Digite o ID da conta a pagar que você deseja editar: "))
        editar_conta_a_pagar(id_conta)

    elif menu == "4":
        id_conta = int(input("Digite o ID da conta a receber que você deseja editar: "))
        editar_conta_a_receber(id_conta)

    elif menu == "5":
            contas_a_pagar = buscar_contas_a_pagar()
            print(100*"-")
            print("Contas a pagar")
            for conta in contas_a_pagar:
                print(conta)  # Imprimir ou formatar as informações conforme necessário
            print(100*"-")
            
    elif menu == "6":
            print(100*"-")
            print("contas a receber")
            contas_a_receber = buscar_contas_a_receber()
            for conta in contas_a_receber:
                print(conta)  # Imprimir ou formatar as informações conforme necessário
            print(100*"-")

    elif menu == "7":
        id_conta = int(input("Digite o id da conta que deseja deletar: "))
        deletar_conta_a_pagar(id_conta)
        print('Conta deletada com sucesso!')
    elif menu == "8":
        id_conta = int(input("Digite o id da conta que deseja deletar: "))
        deletar_conta_a_receber(id_conta)
        print('Conta deletada com sucesso!')

    elif menu == "9":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
        
# Fechando a conexão ao final
conexao.close()
