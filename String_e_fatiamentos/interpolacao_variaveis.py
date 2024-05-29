nome= "Isabela"
idade= 25
profissao= "Programador"
linguagem= "Python"

print("Nome: %s, Idade: %d, profissão: %s, estudo: %s." % (nome, idade, profissao, linguagem))

print("Nome: {}, Idade: {}, profissão: {}, estudo: {}." . format(nome, idade, profissao, linguagem))

print(f"Nome: {nome}, idade: {idade} profissão: {profissao}, estudo:{linguagem}.")

#formatação simplificada
PI=3.14159
print(f"O valor de PI: {PI: .2F}")
print(f"O valor de PI: {PI:10.2F}") # 10 EQUIVALENTE AO NUMERO DE ESPACOS E 2 AO NUMERO DE CASAS PARA MSOTRAR O RESULTADO