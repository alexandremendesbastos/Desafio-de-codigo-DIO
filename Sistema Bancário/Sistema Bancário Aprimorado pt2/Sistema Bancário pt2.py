def menu_init():
    print("""\n
    ================ MENU ================
    [1]\tAccess Account
    [2]\tCreate Account
    [0]\tExit """)

    option_init = int(input("\t=> "))
    return option_init

def account_access(amount_accounts, contas, id_conta, saldo, extrato, agency, back):
    option_init = menu_init()


    if option_init == 1:
        if amount_accounts == 0:
            print("Before accessing, create at least one account")
            new_account(contas, id_conta, saldo, extrato, agency, amount_accounts)
            amount_accounts += 1
            account_access(amount_accounts, contas, id_conta, saldo, extrato, agency, back)
        else:
            id_consulta = int(input("Account number: "))
            verify_pass = input("Enter the password for this account: ")

            if verify_pass == contas[id_consulta]['senha'] and id_consulta in contas:
                print("\n============ WELCOME AGAIN ============\n")
                print(f"ID: {id_consulta}, Agency: {contas[id_consulta]['agency']} Name: {contas[id_consulta]['nome']}")
            else:
                print("Account does not exist.")

    elif option_init == 2:
        new_account(contas, id_conta, saldo, extrato, agency, amount_accounts)
        amount_accounts += 1
        account_access(amount_accounts, contas, id_conta, saldo, extrato, agency, back)

    elif option_init == 0:
        print("=== BYE-BYE ===")
        back = 0

    else:
        print("Invalid option, try again!")
        account_access(amount_accounts, contas, id_conta, saldo, extrato, agency, back)
    return back

def kit(back):
    back = back
    return back

def menu():
    print("""\n
    ================ MENU ================
    [1]\tDeposit
    [2]\tWithdraw
    [3]\tStatement
    [4]\tNew Account
    [5]\tList Accounts
    [0]\tExit """)

    option = int(input("\t=> "))
    return option

def new_account(contas, id_conta, saldo, extrato, agency, amount_accounts):
    id_conta += 1
    name = input("User name: ")
    senha_user = input("Password: ")

    while len(senha_user) < 8:
        senha_user = input("The password is too short, please try again!")
        if senha_user == "0":
            break

    nova_conta = {
        'id': id_conta,
        'agency': agency,
        'nome': name,
        'saldo': saldo,
        'extrato': extrato,
        'senha': senha_user
    }

    contas[id_conta] = nova_conta
    print(f"New account successfully created!\nID: {id_conta}, Agency: {contas[id_conta]['agency']} Name: {contas[id_conta]['nome']}")

    amount_accounts += 1
    return contas, id_conta, saldo, extrato, amount_accounts

def display_accounts(contas):
    id_consulta = int(input("Account number: "))
    verify_pass = input("Enter the password for this account: ")

    if verify_pass == contas[id_consulta]['senha'] and id_consulta in contas:
        print(f"ID: {id_consulta}, Agency: {contas[id_consulta]['agency']} Name: {contas[id_consulta]['nome']}")
    else:
        print("Account not found.")

def deposit(saldo, extrato, numero_saques):
    valor_deposito = float(input("Deposit amount: "))

    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"\tDeposit: ${valor_deposito:.2f}\n"
        print(f"Deposit of ${valor_deposito:.2f} successfully made!\n")
        numero_saques += 1
    else:
        print("Invalid value!")

    return saldo, extrato, numero_saques

def withdraw(saldo, numero_saques, limite, limite_saques, quant_operacoes, extrato):
    saque = float(input("Withdrawal amount: \n=> "))

    if saque > limite:
        print("Withdrawal amount exceeds the allowed limit!\n")

    elif saque <= 0:
        print("Amount below the minimum, unable to process the transfer!\n")

    elif numero_saques >= limite_saques:
        print("Withdrawal limit exceeded, please try again tomorrow!\n")

    elif saque > saldo:
        print("You do not have enough balance for this operation!")

    else:
        saldo -= saque
        print(f"\nWithdrawal of ${saque:.2f} successfully made!\n")
        extrato += f"\tWithdrawal: ${saque:.2f}\n"
        numero_saques += 1
        quant_operacoes += 1

    return saldo, numero_saques, extrato, quant_operacoes

def display_statement(extrato, quant_operacoes):
    if quant_operacoes == 0:
        extrato += "No transactions have been made on this account yet!\n"

    print(extrato)

def main():
    quant_operacoes = 0
    limite_saques = 3
    agency = 1
    saldo = 0
    limite = 500
    extrato = "\t______---__-STATEMENT-__---______\n"
    numero_saques = 0
    contas = {}
    id_conta = 0
    amount_accounts = 0
    back = 1


    back = amount_accounts= account_access(amount_accounts, contas, id_conta, saldo, extrato, agency, back)


    while True:
        back = kit(back)
        if back == 0:
            break

        option = menu()

        if option == 0:
            print(contas)
            break

        elif option == 1:
            saldo, extrato, numero_saques = deposit(saldo, extrato, numero_saques)

        elif option == 2:
            saldo, numero_saques, extrato, quant_operacoes = withdraw(
                saldo, numero_saques, limite, limite_saques, quant_operacoes, extrato
            )

        elif option == 3:
            display_statement(extrato, quant_operacoes)

        elif option == 4:
            contas, id_conta, saldo, extrato, amount_accounts = new_account(
                contas, id_conta, saldo, extrato, agency, amount_accounts
            )

        elif option == 5:
            display_accounts(contas)


if __name__ == '__main__':
    main()