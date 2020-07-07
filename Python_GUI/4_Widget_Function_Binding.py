from tkinter import *

root = Tk()

# Function accepts an event as a parameter
def printName(event):
    print("Hello my name is name!")

# Using either bind OR command to bind function to be executed when button is clicked
# You can use the command and bind at the same time.
button_1 = Button(root, text = "Print my name") #, command = printName)
button_1.bind("<Button-1>", printName) # Button-1 is the left mouse button
button_1.pack()

root.mainloop()
