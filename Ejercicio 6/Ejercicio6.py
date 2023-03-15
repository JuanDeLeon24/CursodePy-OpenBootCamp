class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

# Crear objeto de la clase Coche
mi_coche = Coche('Rojo', 4, 5, 200, 2000)

# Mostrar atributos del objeto creado
print(f"Color: {mi_coche.color}")
print(f"Ruedas: {mi_coche.ruedas}")
print(f"Puertas: {mi_coche.puertas}")
print(f"Velocidad: {mi_coche.velocidad}")
print(f"Cilindrada: {mi_coche.cilindrada}")
