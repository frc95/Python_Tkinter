from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Hola Mundo')

#imagen = Image.open('computer.jpg')
#imagen.show()

img = ImageTk.PhotoImage(Image.open('computer.jpg'))
l = Label(image=img)
l.pack()

root.mainloop()

