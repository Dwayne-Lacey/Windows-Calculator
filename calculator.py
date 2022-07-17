from tkinter import *

class CalcEntry(Entry):
    # Constructs entry box object as part of CalcEntry object, *kwargs allows us to pass as many parameters to the entry box as we would like
    # Entry class variable is where values will be stored for addition
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.last_operator = None
        self.value_totalled = False
        self.current_value = None

    # Adds numbers to entry box
    def enter_numbers(self, number):
        if self.value_totalled == True:
            self.clear_entry()
            self.value_totalled = False
        self.insert(END, number)

    # Clears entry field
    def clear_entry(self):
        self.delete(0, END)
    
    # Function to check what value to return from entry box
    def return_entry_number(self):
        print(self.get())
        if len(self.get()) == 0:
            value_to_return = 0
        else:
            value_to_return = float(self.get())
        return value_to_return

    # # Performs addition when "+" button is pressed
    # def addition(self):
    #     value = self.return_entry_number()
    #     self.current_value += value
    #     self.last_operator = "+"
    #     print(self.current_value)
    #     self.clear_entry()

    # # Performs subtraction when "-" button is pressed
    # def subtraction(self):
    #     value = self.return_entry_number()
    #     self.current_value -= value
    #     self.last_operator = "-"
    #     print(self.current_value)
    #     self.clear_entry()
        
    # # Performs multiplication when "*" button is pressed
    # def multiplication(self):
    #     value = self.return_entry_number()
    #     self.current_value *= value
    #     self.last_operator = "*"
    #     print(self.current_value)
    #     self.clear_entry()

    # # Performs division when "/" button is pressed
    # def division(self):
    #     value = self.return_entry_number()
    #     self.current_value /= value
    #     self.last_operator = "/"
    #     print(self.current_value)
    #     self.clear_entry()

    # Function to perform addition/subtraction/multiplication
    def operation(self, operator):
        value = self.return_entry_number()
        if self.current_value == None:
            self.current_value = value
        else:
            if operator == "+":
                self.current_value += value
            elif operator == "-":
                self.current_value -= value
            elif operator == "*":
                self.current_value *= value
            elif operator == "/":
                self.current_value /= value
        self.last_operator = operator
        self.clear_entry()
    # Performs calculations when equal button is pressed
    def calculate(self):
        self.operation(self.last_operator)
        self.insert(0, self.current_value)
        self.current_value = None
        self.value_totalled = True

# Builds main window
root = Tk()

# Adds title to window
root.title("Simple Calculator")

# Creates entrybox
entry = CalcEntry(root, width=55, borderwidth=5)

# Places entry box on window
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)



# Creates number pad buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: entry.enter_numbers(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: entry.enter_numbers(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: entry.enter_numbers(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: entry.enter_numbers(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: entry.enter_numbers(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: entry.enter_numbers(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: entry.enter_numbers(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: entry.enter_numbers(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: entry.enter_numbers(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: entry.enter_numbers(0))

# Creates buttons holding calculation functions and clear function
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: entry.operation("+"))
button_subtract = Button(root, text="-", padx=39, pady=20, command=lambda: entry.operation("-"))
button_multiply = Button(root, text="*", padx=39, pady=20, command=lambda: entry.operation("*"))
button_divide = Button(root, text="/", padx=39, pady=20, command=lambda: entry.operation("/"))
button_equal = Button(root, text="=", padx=39, pady=20, command=entry.calculate)
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

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=5, column=3, columnspan=1)

# Maintains application loop until retrieving input to close application
root.mainloop()