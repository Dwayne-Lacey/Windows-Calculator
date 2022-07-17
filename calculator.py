from tkinter import *

class CalcEntry(Entry):
    # Constructs entry box object as part of CalcEntry object, *kwargs allows us to pass as many parameters to the entry box as we would like
    # Entry class variable is where values will be stored for addition
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.entry = []
        self.value_total = False
    # Adds numbers to entry box
    def button_click(self, number):
        if self.value_total == True:
            self.clear_entry()
            self.value_total = False
        self.insert(END, number)

    # Clears entry field
    def clear_entry(self):
        self.delete(0, END)
    
    # Adds each number to be added into a list
    def add_click(self):
        self.entry.append(int(self.get()))
        print(self.entry)
        self.clear_entry()
        
    # Calculates total of all numbers in list
    def calculate_list(self):
        self.add_click()
        self.clear_entry()
        total = 0
        for num in self.entry:
            total += num
        self.insert(0, total)
        self.value_total = True
        self.entry = []

# Builds main window
root = Tk()

# Adds title to window
root.title("Simple Calculator")

# Creates entrybox
entry = CalcEntry(root, width=45, borderwidth=5)

# Places entry box on window
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)



# Creates number pad buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: entry.button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: entry.button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: entry.button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: entry.button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: entry.button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: entry.button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: entry.button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: entry.button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: entry.button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: entry.button_click(0))
button_add = Button(root, text="+", padx=39, pady=20, command=entry.add_click)
button_equal = Button(root, text="=", padx=91, pady=20, command=entry.calculate_list)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=entry.clear_entry)

# Adds buttons to grid
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)

# Maintains application loop until retrieving input to close application
root.mainloop()