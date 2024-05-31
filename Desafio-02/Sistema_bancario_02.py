import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [D]\tDepositar
    [S]\tSacar
    [E]\tExtrato
    [NC]\tNova conta
    [LC]\tListar contas
    [NU]\tNovo usuário
    [X]\tSair
    => """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\nXXX ATENÇÃO!O valor informado é inválido. Tente novamente XXX")
  
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n XXX Operação falhou! Você seu saldo é insuficiente. XXX")

    elif excedeu_limite:
        print("\n XXX Operação falhou! O valor do saque ultrapassa o limite para saques diários. XXX")

    elif excedeu_saques:
        print("\n XXX Operação falhou! Quantidade máxima de saques excedida. XXX")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\nXXX Operação falhou! O valor informado é inválido. XXX")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    while True:
        cpf = input("Informe o CPF (somente números): ")

        # Verifica se o CPF tem exatamente 11 dígitos e se são números
        if len(cpf) != 11 or not cpf.isdigit():
            print("\nXXX CPF inválido! O CPF deve conter exatamente 11 dígitos numéricos. XXX")
        else:
            usuario = filtrar_usuario(cpf, usuarios)

            if usuario:
                print("\nXXX Já existe usuário com esse CPF! XXX")
                return

            nome = input("Informe o nome completo: ")
            data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
            endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

            usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

            print("=== Usuário criado com sucesso! ===")
            break  # Sai do loop while True após criar o usuário com sucesso



def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nXXX Usuário não encontrado, não foi possível abrir sua conta neste momento! XXX")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "D":
            valor = float(input("Informe o valor para depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "E":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "NU":
            criar_usuario(usuarios)

        elif opcao == "NC":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "LC":
            listar_contas(contas)

        elif opcao == "X":
            break

        else:
            print("Operação inválida, informe uma opção válida!")


main() 
