from tkinter import *

# Builds main window
root = Tk()

# Creates button on screen saying click me
button = Button(root, text="Click Me!", padx=50, pady=50)

# Places button on window
button.pack()

root.mainloop()