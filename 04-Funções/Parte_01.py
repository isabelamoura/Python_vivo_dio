def exibir_mensagem():
    print("Olá estudante!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Isabela")
exibir_mensagem_3()
exibir_mensagem_3(nome="Pedro")

