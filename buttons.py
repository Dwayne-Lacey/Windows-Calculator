from tkinter import *

# Builds main window
root = Tk()

# Adds label object below current packed object on screen
def myClick():
    label = Label(root, text="I clicked this button!")
    label.pack()

# Creates button on screen saying click me
button = Button(root, text="Click Me!", padx=50, pady=50, command=myClick)

# Places button on window
button.pack()

root.mainloop()