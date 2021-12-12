from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Hola mundo')

#def click():
    #messagebox.showwarning('Popup', 'Hola mundo')

#def click():
    #messagebox.showinfo('Popup', 'Hola mundo')

#def click():
    #messagebox.showerror('Popup', 'Hola mundo')

#def click():
    #respuesta = messagebox.askquestion('Popup', 'Hola mundo')
    #if respuesta == 'yes':
        #messagebox.showinfo('Respuesta', 'la respuesta fue ' + respuesta)
    #else:
        #messagebox.showinfo('Respuesta', ':( la respuesta fue ' + respuesta)

#def click():
    #repuesta = messagebox.askokcancel('Hola mundo', 'Desea realizar accion')
    #if repuesta:
        #messagebox.showinfo('Hola mundo', 'La respuesta fue OK')
    #else:
        #messagebox.showinfo('Hola mundo', 'La respuesta fue cancelar')

def click():
    repuesta = messagebox.askyesno('Hola mundo', 'Desea realizar accion')
    if repuesta:
        messagebox.showinfo('Hola mundo', 'La respuesta fue OK')
    else:
        messagebox.showinfo('Hola mundo', 'La respuesta fue cancelar')

btn = Button(root, text='Presioname', command=click)
btn.pack()

root.mainloop()