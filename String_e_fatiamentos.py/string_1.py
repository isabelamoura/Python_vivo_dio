nome = "Isabela"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Ola mundo!    "
print(texto)
print(texto.strip() + ".")
print(texto.lstrip() + ".")
print(texto.rstrip() + ".")

menu = "Python"


print("####"+ menu + "####") 
print(menu.center(14)) #Para centralizar o menu sem os #
print(menu.center(20, "#")) # 14 é a quantidade de # que quero que tenha centralizado
print("P-y-t-h-o-n")
print("-".join(menu)) #Para adicionar - entre as letras

