frutas= ("maçã", "laranja", "uva", "pera",)
print(frutas[-1])
print(frutas[-3])

matriz= (

    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)


print(matriz[0])
print(matriz[0] [0]) #PRIMEIRA LINHA, PRIMEIRA COLUNA
print(matriz[0][-1]) #PRIMEIRA LINHA, ULTIMA COLUNA
print(matriz[-1][-1]) #ULTIMA LINHA, ULTIMA COLUNA


tupla= ("p", "y", "t", "h", "o", "n",)
        
print(tupla[2:], "\n") #START
print(tupla[:2], "\n") #STOP
print(tupla[1:3], "\n") #START, STOP
print(tupla[0:3:2], "\n") #START, STOP, STEP (PRIMEIRO E TERCEIRO ITEM, INDO DE 2 EM 2)
print(tupla[::], "\n")
print(tupla[:-1], "\n")


carros = ("gol")
print(isinstance(carros, tuple))