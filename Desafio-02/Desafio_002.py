def recomendar_plano(consumo):
    if consumo <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    
    elif consumo <= 20:
        return "Plano Prata Fibra - 100Mbps"
    
    else:
        return "Plano Premium Fibra - 300Mbps"


consumo_usuario = float(input("Por favor, informe o consumo médio mensal de dados em GB: "))
plano_recomendado = recomendar_plano(consumo_usuario)
print("O plano recomendado para o seu consumo é:", plano_recomendado)
