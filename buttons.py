from tkinter import *

# Builds main window
root = Tk()

# Creates entrybox
entry = Entry(root)

# Places entry box on window
entry.pack()

# Enters default text into entry box
entry.insert(0, "Enter your name:")

# Adds label object below current packed object on screen
def myClick():
    label = Label(root, text="I clicked this button!")
    label.pack()

# Function to store entry and create label stating user has logged in
def store_entry():
    # get() function retrieves text from entry box
    text = "I've been watching you " + entry.get()
    label2 = Label(root, text=text)
    label2.pack()

# Creates button on screen saying click me
button = Button(root, text="Click Me!", padx=50, pady=50, command=myClick)

# Creates new button with command to retrieve text from entry box
entry_button = Button(root, text="Retrieving entry box text", command=store_entry)

# Places button on window
button.pack()
entry_button.pack()

# Maintains application loop until retrieving input to close application
root.mainloop()