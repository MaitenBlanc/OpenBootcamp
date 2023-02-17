class Color:
    color = "Rojo"

class Ruedas:
    cantidadRuedas = 4

class Puertas:
    cantidadPuertas = 5

class Vehiculo:
    color = Color()
    ruedas = Ruedas()
    puertas = Puertas()

class Coche(Vehiculo):
    velocidad = 120
    cilindrada = 1500

c = Coche()
print("Color:", c.color.color)
print("Ruedas: ", c.ruedas.cantidadRuedas)
print("Puertas: ", c.puertas.cantidadPuertas)
print("Velocidad: ", c.velocidad)
print("Cilindrada: ", c.cilindrada)