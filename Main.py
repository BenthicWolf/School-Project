
import tkinter
from tkinter import *


def Pressed():
    pass


label1 = tkinter.Label(
    text="Hello",
    fg="white",
    bg="navy blue",
    width=200,
    height=200
)


def createntry():
    label2 = tkinter.Label(text="Enter your text", height=5)
    entry = tkinter.Entry(width=50)
    button1 = tkinter.Button(label2, text="Input Text", command=Pressed)

    label2.pack()
    button1.pack()
    entry.pack()


def createwindow():
    window = tkinter.Tk()
    window.geometry("400x400")
    window.title("Project")
    label1.pack()


createntry()
# createwindow()

label1.mainloop()
