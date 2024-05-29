frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

##PARA LISTAR NUMEROS#


numeros = [1, 30, 21, 20, 9, 44, 65, 34]                           #PARA IMPRIMIR APENAS NUMEROS PARES
pares = [numero for numero in numeros if numero % 2 == 0]          #PARA IMPRIMIR APENAS NUMEROS PARES
                                                                   #PARA IMPRIMIR APENAS NUMEROS PARES
print("Números pares:")
for numero in pares:
    print(numero)
                                            
quadrado=[]
for numero in numeros:
    quadrado.append(numero ** 2)                                     #APPEND PARA ADICIONAR UM ELEMENTO AO FINAL                                
    print(quadrado)

  