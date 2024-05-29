#ORDENAR POR ORDEM ALFABETICA


linguagens = ["python", "js", "c", "java", "csharp"]


print(sorted(linguagens, key=lambda x: len(x)))
print()
print(sorted(linguagens, key=lambda x: len(x), reverse= True))
print()

print(sorted(linguagens))