from tkinter import *

root = Tk()

label_1 = Label(root, text = "Name")
label_2 = Label(root, text = "Password")
entry_1 = Entry(root) # A field that holds visibly typed text
entry_2 = Entry(root)

# Grid layout doesnt take up, down etc. Only N, E, S or W
# Grid layout also doesn't use pack like frames.
label_1.grid(row = 0, sticky = E) # sticky right aligns text. Top left
label_2.grid(row = 1, sticky = E) # Bottom left

entry_1.grid(row = 0, column = 1) # Top right
entry_2.grid(row = 1, column = 1) # Bottom right

c = Checkbutton(root, text = "Keep me logged in.")
c.grid(columnspan = 2)
# c is added to the bottom of the grid

root.mainloop()