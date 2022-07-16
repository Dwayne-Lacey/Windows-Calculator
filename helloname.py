from tkinter import *

# Creates new window
root = Tk()

# Creates label widgets
label1 = Label(root, text="Hello World")
label2 = Label(root, text="My name is Dwayne")

# Places labels on screen
label1.grid(row=0, column=0)
label2.grid(row=1, column=1)

# Application main loop
root.mainloop()
