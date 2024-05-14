MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
else:
    print("Ainda não pode tirar CNH.")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar CNH.")
