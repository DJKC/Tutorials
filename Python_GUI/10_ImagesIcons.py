from tkinter import *

root = Tk()

photo = PhotoImage(file = "bloom.png")
label = Label(root, image = photo)
label.pack()

root.mainloop()