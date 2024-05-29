lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()  # PARA CRIAR UMA CÓPIA

print(lista)

print(id(l2), id(lista))  # PARA VERIFICAR SE SÃO OBJETOS DIFERENTES

l2[0] = 2

print(l2)
print(lista)
