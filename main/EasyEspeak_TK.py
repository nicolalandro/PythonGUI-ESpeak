import os

from tkinter import *

# import os  # Serve per la riga di comando
from Speaker import speack

root = Tk()
root.title('Simple Espeack')
root.resizable(0, 0)  # Resizable false

label1 = Label(root, text="Insert Here Text, without special character")
label1.pack()

checkValue = IntVar()
c = Checkbutton(root, text="it/mb-it4", variable=checkValue)
c.pack()

textArea1 = Text(root)
textArea1.pack()


def callback():
    speack(textArea1.get("1.0", END), checkValue.get())

button1 = Button(root, text="Speak", command=callback)
button1.pack()

root.mainloop()
