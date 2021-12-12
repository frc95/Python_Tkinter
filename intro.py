from tkinter import *

root = Tk()
root.title('Hola mundo')
root.geometry('400x400')

l1 = Label(root, text='Hola mundo mi primera etiqueta')
l2 = Label(root, text='Chau mundo mi segunda etiqueta')
l3 = Label(root, text='           ')
#Label(root, text='Hola mundo mi primera etiqueta').pack()

#l1.pack()
l1.grid(row=0, column=0)
l2.grid(row=10, column=10)
l3.grid(row=1, column=1)

root.mainloop()