from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "Don't forget to blink")

answer = tkinter.messagebox.askquestion("Q1", "Are you alive:")

if(answer == "yes"):
    print("You answered yes.")

root.mainloop()
