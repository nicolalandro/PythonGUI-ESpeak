import os

from tkinter import *

# import os  # Serve per la riga di comando

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
    if checkValue.get() == 1:
        uno = 'espeak -v mb-it4 "'
    else:
        uno = 'espeak -v it "'
    due = textArea1.get("1.0", END)
    tre = '"'

    discorso = uno + due + tre
    discorso = discorso.encode("utf8")

    os.system(discorso)


button1 = Button(root, text="Speak", command=callback)
button1.pack()

root.mainloop()
