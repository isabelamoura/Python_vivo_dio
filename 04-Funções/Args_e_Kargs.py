def exibir_poema(data_extenso, *args, **kargs):
    texto = "\n".join(args)
    meta_dados= "\n".join([f"{chave.title()}: {valor}" for chave, valor in kargs.items()])   #.itens porque ele é um dicionário#
    mensagem= f"{data_extenso}\n\n {texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Quinta-feira, 30 de Maio de 2024",
    "Zen of Python",
    "Beautiful is better than ugly.",
    "Beautiful is better than ugly.",
    "Beautiful is better than ugly.",
    "Beautiful is better than ugly.",
    "Beautiful is better than ugly.",
    "Beautiful is better than ugly.",
    "Beautiful is better than ugly.",
    "Beautiful is better than ugly.",
    "Beautiful is better than ugly.",
    "Beautiful is better than ugly.",
    "Beautiful is better than ugly.",
       autor= "Tim Petters", ano=1999
)