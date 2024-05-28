# Solicitar dados da agência e da conta com validação
while True:
    agencia = input("Informe o número da agência (4 dígitos): ")
    if len(agencia) == 4 and agencia.isdigit():
        break
    else:
        print("Agência inválida! A agência deve conter exatamente 4 dígitos numéricos.")

while True:
    conta = input("Informe o número da conta (6 dígitos): ")
    if len(conta) == 6 and conta.isdigit():
        break
    else:
        print("Conta inválida! A conta deve conter exatamente 6 dígitos numéricos.")
menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[X] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:  # Loop infinito
    
    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
        else:
            print("Não é possível realizar esta operação! O valor informado é inválido.")

    elif opcao == "S":
        valor = float(input("Informe o valor do saque: "))          

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Não é possível realizar a operação! Você não possui saldo suficiente.")
        elif excedeu_limite:
            print("Não é possível realizar a operação! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Não é possível realizar esta operação! Número de saques diários excedidos.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "E":
        print("\n================EXTRATO================")
        print(f"Agência: {agencia} | Conta: {conta}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("=======================================")

    elif opcao == "X":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada.")
