conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b))  # NAO POSSUI RELACAO ENTRE ELES
print(conjunto_a.isdisjoint(conjunto_c))  # O 1 FAZ RELACAO ENTRE ELES
