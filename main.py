class Vehiculo():
    color = None
    ruedas = None
    puertas = None

    def __init__(self):
        self.color = "Rojo"
        self.ruedas = 4
        self.puertas = 5

class Coche(Vehiculo):
    velocidad = None
    cilindrada = None

    def __init__(self):
        super().__init__()
        self.velocidad = 120
        self.cilindrada = 500

coche = Coche()
print("Color:", coche.color)
print("Número de ruedas:", coche.ruedas)
print("Número de puertas:", coche.puertas)
print("Velocidad:", coche.velocidad)
print("Cilindrada:", coche.cilindrada)