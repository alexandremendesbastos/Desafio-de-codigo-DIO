def menu():
    print("""\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tListar contas
    [0]\tSair """)

    global option
    option = int(input("=> "))

def nova_conta(contas, id_conta, saldo, extrato, agencia):
    id_conta += 1
    nome = input("User name: ")
    senha_user = input("Password: ")
    while len(senha_user) < 8:
        senha_user = input("the password is very short, pls try again!")
        if senha_user == 0:
            break


    # Cria um dicionário interno para armazenar os dados da conta
    conta = {
        'id': id_conta,
        'agencia': agencia,
        'nome': nome,
        'saldo': saldo,
        'extrato': extrato,
        'senha': senha_user
        }
    # Adiciona o dicionário da conta ao dicionário de contas principal
    contas[id_conta] = conta

    print("Nova conta criada com sucesso!")

    return conta, contas, id_conta, saldo, extrato

def exibe_contas(conta):
    id_consulta = int(input("Número da conta: "))
    verifica_senha = input(" digite a senha desta conta: ")

    if verifica_senha in {conta[id_consulta]['senha']} and id_consulta in conta:
        print(f"ID: {id_consulta}, Agencia: {conta[id_consulta]['agencia']} Nome: {conta[id_consulta]['nome']}")
    else:
        print("Conta não encontrada.")
def depositar(saldo, extrato, numero_saques):
    global valor_deposito
    valor_deposito = float(input("Valor do depósito: "))

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"\tDepósito: R${valor_deposito:.2f}\n"
        print(f"Depósito no valor de R${valor_deposito:.2f} realizado com sucesso!\n")
        numero_saques += 1

    else:
        print("Valor inválido!")

    return saldo, extrato, numero_saques


def sacar(saldo, numero_saques, limite, limite_saques, quant_operacoes, extrato):
    saque = float(input("Valor do saque: \n=> "))

    if saque > limite:
        print("Saque maior que o limite permitido!\n")

    elif saque <= 0:
        print("Valor abaixo do mínimo, impossível realizar a transferência!\n")

    elif numero_saques >= limite_saques:
        print("Limite de saques excedido, tente novamente amanhã!\n")

    elif saque > saldo:
        print("Você não possui saldo para esta operação!")

    else:
        saldo -= saque
        print(f"\nSaque de R${saque:.2f} realizado com sucesso!\n")
        extrato += f"\tSaque: R${saque:.2f}\n"
        numero_saques += 1
        quant_operacoes += 1

    return saldo, numero_saques, extrato, quant_operacoes


def exibe_extrato(extrato, quant_operacoes):
    if quant_operacoes == 0:
        extrato += "Ainda não ocorreram movimentações nesta conta!\n"

    print(extrato)

def main():
    quant_operacoes = 0
    limite_saques = 3
    agencia = 1
    saldo = 0
    limite = 500
    extrato = "\t______---__-EXTRATO-__---______\n"
    numero_saques = 0
    contas = {}
    id_conta = 0
    quant_contas = 0
    while True:

        if quant_contas == 0:
            print("Crie uma conta para poder utilizar o sistema")

            _, contas, id_conta, saldo, extrato = nova_conta(contas, id_conta, saldo, extrato, agencia)
            quant_contas += 1
            continue

        menu()

        if option == 1:
            saldo, extrato, numero_saques = depositar(saldo, extrato, numero_saques)

        elif option == 2:
            saldo, numero_saques, extrato, quant_operacoes = sacar(saldo, numero_saques, limite, limite_saques,
                                                                   quant_operacoes, extrato)

        elif option == 3:
            exibe_extrato(extrato, quant_operacoes)

        elif option == 4:
            _, contas, id_conta, saldo, extrato = nova_conta(contas, id_conta, saldo, extrato, agencia)

        elif option == 5:
            exibe_contas(contas)

        elif option == 0:
            print(contas)
            break


if __name__ == '__main__':
    main()