from tkinter import *

# Builds main window
root = Tk()

# Adds title to window
root.title("Simple Calculator")

# Creates entrybox
entry = Entry(root, width=35, borderwidth=5)

# Places entry box on window
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# Maintains application loop until retrieving input to close application
root.mainloop()