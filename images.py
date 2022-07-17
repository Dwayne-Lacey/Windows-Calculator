from tkinter import *

# Create new window
root = Tk()

# Title of window
root.title("Images")

# Changing window icon, file path where icon located
root.iconbitmap('C:/Users/Dwayne/Downloads/test.ico')

# Button to quit out of application
button_quit = Button(root, text="Exit Program", command=root.quit)






# Loops window until receiving input to close window
root.mainloop()