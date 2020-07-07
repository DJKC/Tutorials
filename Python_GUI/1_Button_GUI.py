from tkinter import *

root = Tk()

# A frame is responsible for holding objects, visible or not
# Root is a base that all frames must bind to
topFrame = Frame(root)
topFrame.pack() # Pack allows the frame changes to become part of the frame
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM) # BOTTOM is explicit so top is now on TOP

# Buttons 1-3 are on a separate frame than B#4
button1 = Button(topFrame, text = "Button #1", fg = "red")
button2 = Button(topFrame, text = "Button #2", fg = "orange")
button3 = Button(topFrame, text = "Button #3", fg = "yellow")
button4 = Button(bottomFrame, text = "Button #4", fg = "green")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = BOTTOM)

# Keeps the frame visible on the screen during the whole execution
root.mainloop()