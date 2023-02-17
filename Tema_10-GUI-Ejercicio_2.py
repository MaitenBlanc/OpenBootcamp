from tkinter import *

window = Tk()

elemento = StringVar()

listbox = Listbox(window)

listbox.insert(END, "Ford", "Chevrolet", "Peugeot", "Fiat", "Renault")
listbox.pack()

label = Label(text="Marcas de autos")
label.pack()


window.mainloop()