
import tkinter
from tkinter import *


def Pressed():
    pass


def createwindow():
    window = tkinter.Tk()
    window.geometry("400x400")
    window.title("Project")

    label = tkinter.Label(
        text="Hello",
        fg="white",
        bg="navy blue",
        width=200,
        height=200
    )
    button1 = tkinter.Button(
        text="Press",
        width=10,
        height=10,
        bg="grey"
    )

    label.pack()
    window.mainloop()


createwindow()
