def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:
        return "Plano Premium Fibra - 300Mbps"

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Por favor, informe o consumo médio mensal de dados em GB: "))

# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print("O plano recomendado é: ", recomendar_plano(consumo))