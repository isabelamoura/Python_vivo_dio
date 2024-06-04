class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):  # SELF - INSTANCIA
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = 19

    def buzinar(self):
        print("BIP BIP")

    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada")

    def correr(self):
        print("Vruummmmmm...")

    # def __str__(self):
        return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        # util para representacao de classes
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("preta", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo)

b2 = Bicicleta("amarela", "monark", 1998, 199)
print(b2)
