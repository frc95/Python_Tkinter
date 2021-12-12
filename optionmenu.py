from tkinter import *

root = Tk()
root.title('Hola mundo: Option menu')
root.geometry('500x500')

def enviar():
    l = Label(root, text=value.get())
    l.pack()


lista = [
    'Muebles', 
    'Cocina', 
    'Electro'
]

value = StringVar()
value.set(lista[2])

drop = OptionMenu(root, value, *lista)
drop.pack()

btn = Button(root, text='Enviar', command=enviar)
btn.pack()

root.mainloop()