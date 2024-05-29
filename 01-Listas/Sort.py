#PARA ORGANIZAR OS ARQUIVOS


linguagens = ["Python", "js", "c", "java", "csharp"]

linguagens.sort()
print(linguagens, "\n")

linguagens.sort(reverse=True)
print(linguagens, "\n")

linguagens.sort(key=lambda x: len(x))
print(linguagens, "\n")

linguagens.sort(key=lambda x: len(x), reverse=True)
print(linguagens, "\n")
