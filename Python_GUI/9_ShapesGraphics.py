from tkinter import *

root = Tk()

canvas = Canvas(root, width = 200, height = 100)
canvas.pack()

# starts in top left corner
blackLine = canvas.create_line(0, 0, 200, 50)  # X1,Y1,X2,Y2
redLine = canvas.create_line(0, 100, 200, 50, fill = "red")  # X1,Y1,X2,Y2
#X1,Y1,WIDTH,HEIGHT
greenBox = canvas.create_rectangle(25, 25, 130, 60, fill = "green")

# canvas.delete(redLine)
# canvas.delete(ALL)

root.mainloop()