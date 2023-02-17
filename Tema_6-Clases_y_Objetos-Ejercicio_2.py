class Alumno:
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def resultado(self):
        if self.nota <= 6:
            print("El alumno no aprobó")
        else:
            print("El alumno aprobó")

a1 = Alumno()
a2 = Alumno()

a1.inicializar("Maitén" , 5)
a2.inicializar("Juan", 9)

a1.imprimir()
a1.resultado()
print("_______________________________")
a2.imprimir()
a2.resultado()


