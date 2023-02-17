from functools import reduce

def listaNumeros(lista):
    impares = list(filter((lambda x: x % 2), lista))
    print(impares)
    impares = reduce((lambda x, y: x + y), impares)
    print("Resultado suma: ", impares)

lista = list(range(100))

listaNumeros(lista)