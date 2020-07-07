from tkinter import *

root = Tk()

one = Label(root, text = "One", bg = "red", fg = "white")
one.pack()# No fill is specified so it will remain the same size

two = Label(root, text = "Two", bg = "green", fg = "black")
two.pack(fill = X) # Two will stretch with the X axis

three = Label(root, text = "Three", bg = "blue", fg = "white")
three.pack(side = LEFT, fill = Y) # Three will stretch with the Y axis

root.mainloop()