from pickle import *

class Vehiculo:
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color

    def __str__(self):
        return f"La marca es {self.marca} y el color es {self.color}"

ford = Vehiculo("ford", "rojo")
print(ford)

f = open('vehiculo_objeto.py', 'w+b')

dump(ford, f)

f.seek(0)
otro_ford = load(f)

print(otro_ford)
f.close()
