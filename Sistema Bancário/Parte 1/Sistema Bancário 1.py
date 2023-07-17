line_menu= "="
print(line_menu * 24)
print(f"{line_menu*3}BEM VINDO AO BANCO{line_menu*3}")
print(line_menu * 24)
menu = ("""
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair
=>
""")
limite = 500
saldo = 0
extrato = ""
numero_saques = 0
limite_saques = 3
numero_operacoes = 0



while True:

    opcao = input(menu)

    if opcao == "d" or "D":
        deposito = float(input("\nvalor do deposito: \n=> "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R${deposito:.2f}\n"
            print(f"deposito no valor de R${deposito:.2f} realizado com sucesso!\n")
            numero_operacoes += 1

        else:
            print("valor inválido!")

    elif opcao == "s" or "S":
        saque = float(input("valor do saque: \n=> "))

        if saque > limite:
            print("saque maior que o limite permitido!\n")

        elif saque <= 0:
            print("valor abaixo do mínimo, impossivel realizar a transfência!\n")

        elif numero_saques >= limite_saques:
            print("limite de saques excedido, tente novamente amanhã!\n")

        elif saque > saldo:
            print("você não possui saldo para esta operação!")

        else:
            saldo = saldo - saque
            print(f"\nSaque de R${saque:.2f} realizado com sucesso!\n")
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1
            numero_operacoes += 1

    elif opcao == "e" or "E":
        if numero_operacoes > 0:
            print(f"Extrato bancario: \nSaldo: R${saldo}\n{extrato}")

        else:
            print(f"Extrato bancario: \nSaldo: R${saldo}\n nenhuma opração foi realizada nesta conta até o momento!")

    elif opcao == "q" or "Q":
        break

    else:
        print("Opção invalida! ")