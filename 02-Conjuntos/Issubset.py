# TODOS ELEMENTOS DE UM SUBCONJUNTO

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b))  # TODOS ELEMENTOS DE A ESTAO EM B
print(conjunto_b.issubset(conjunto_a))

# ISSUPERSET É AO CONTRARIO

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b))  # TODOS ELEMENTOS DE B ESTAO EM A
print(conjunto_b.issuperset(conjunto_a))
