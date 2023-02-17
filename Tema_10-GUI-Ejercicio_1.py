from tkinter import *

def select():
    seleccion = "Seleccionaste la opción " + str(var.get())
    label.config(text=seleccion)

def reset():
    reseteo = var.set(None)
    label.config(text='')

root = Tk()
var = StringVar()
var.set(None)
R1 = Radiobutton(root, text="Opción 1", variable=var, value=1, command=select)
R1.pack(anchor=W)

R2 = Radiobutton(root, text="Opción 2", variable=var, value=2, command=select)
R2.pack(anchor=W)

R3 = Radiobutton(root, text="Opción 3", variable=var, value=3, command=select)
R3.pack(anchor=W)

label = Label(root)
label.pack()
Button(root, text='Reiniciar', command=reset).pack()

root.mainloop()