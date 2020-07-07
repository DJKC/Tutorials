from tkinter import *


class BuckButtons:

    def __init__(self, master): # master is main windows aka root here
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text = "Print message", command = self.printMessage)
        self.printButton.pack(side = LEFT)

        self.quitButton = Button(frame, text = "quit", command = frame.quit)
        self.quitButton.pack(side = LEFT)


    def printMessage(self):
        print("This works!")


root = Tk()
b = BuckButtons(root)
root.mainloop()