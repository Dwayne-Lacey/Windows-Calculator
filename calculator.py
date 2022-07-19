from tkinter import *
from math import sqrt

class CalcEntry(Entry):
    # Constructs entry box object as part of CalcEntry object, *kwargs allows us to pass as many parameters to the entry box as we would like
    # Entry class variable is where values will be stored for addition
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        self.last_operator = None
        self.value_totalled = False
        self.current_value = None



# Standard commands for normal number entry, calculations, and field clearing
    # Adds numbers to entry box
    def enter_numbers(self, number):
        if self.value_totalled == True:
            self.clear_entry()
            self.value_totalled = False
        self.insert(END, number)

    # Clears entry field
    def clear_entry(self):
        self.delete(0, END)
        
    # Clear stored number and current text in entrybox
    def clear_all(self):
        self.clear_entry()
        self.value_totalled = False
        self.current_value = None
        self.last_operator = None

    # Backspace button: Deletes only the last number currently entered into the entrybox
    def backspace(self):
        num_characters = len(self.get())
        self.delete(num_characters - 1, END)

    # Function to perform addition/subtraction/multiplication/division
    def operation(self, operator, value=None):
        if value == None:
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
        self.current_value = self.check_num_type(self.current_value)
        self.insert(0, self.current_value)
        self.current_value = None
        self.value_totalled = True

    # Function to check what value to return from entry box
    def return_entry_number(self):
        print(self.get())
        # Checks if value exists currently within entry box, defaults to 0 if value does not exist.
        if len(self.get()) == 0:
            value_to_return = 0
        else:
            value_to_return = self.check_num_type(self.get())
        return value_to_return

    # Checks if value is a float or an integer and returns value as corresponding type
    def check_num_type(self, value):
        if float(value) // 1 == float(value):
            if self.get().count('.') > 0:
                split_float = self.get().split('.')
                value_to_return = int(split_float[0])
            else:
                value_to_return = int(value)
        else:
            value_to_return = float(value)
        return value_to_return



# Specialized functions to alter inputs or use special calculations on a value
    # Pos/Neg Input: Converts existing input in entry box from negative to positive or positive to negative
    def pos_neg(self):
        if self.get()[0] == '-':
            self.delete(0, 1)
        else:
            self.insert(0, '-')

    # Decimal Input: Inputs a decimal point. Limit of only 1 decimal point
    def add_decimal(self):
        if self.get().count('.') < 1:
            self.insert(END, '.')
            self.value_totalled = False

    # Square Root function: Takes whatever number is passed into X and returns the square root of X. Example 4 should return 2
    # Can be executed with or without number stored in memory
    def square_root(self):
        value = self.return_entry_number()
        if value == 0:
            self.clear_all()
            self.insert(0, 0)
        else:
            value = self.check_num_type(sqrt(value))
            if self.current_value != None:
                self.operation(value)
            else:
                self.clear_entry()
                self.insert(0, value)
        self.value_totalled = True

    # 1/X function: Takes whatever number is passed into X and returns 1 divided by that number. Example 4 should return .25
    # Can be executed with or without number stored in memory
    def fraction(self):
        value = self.return_entry_number()
        if value == 0:
            self.clear_all()
            self.insert(0, 0)
        else:
            value = self.check_num_type(1 / value)
            if self.current_value != None:
                self.operation(value)
            else:
                self.clear_entry()
                self.insert(0, value)
        self.value_totalled = True
    
    # Exponent function: Takes whatever number is passed into X and returns that number squared. Example 2 should return 4
    # Can be executed with or without number stored in memory
    def exponent(self):
        value = self.return_entry_number()
        value = self.check_num_type(value ** 2)
        if self.current_value != None:
            self.operation(value)
        else:
            self.clear_entry()
            self.insert(0, value)
        self.value_totalled = True

    # Percent function: Requires number stored in memory and a second number, function multiplies first and second numbers and then divides the result by 100 to get what percent num2 percent of num1
    # Uses last operator stored to decide if result should be added/subtracted etc. to first number
    def find_percent(self):
        value = self.return_entry_number()
        if self.current_value == None:
            self.clear_entry()
            self.insert(0, 0)
        else:
            percent_value = self.check_num_type((value * self.current_value) / 100)
            self.operation(self.last_operator, percent_value)
            


class Calculator:
    def __init__(self):
        # Builds main window
        self.root = Tk()

        # Adds title to window
        self.root.title("Simple Calculator")

        # Creates entrybox
        self.entry = CalcEntry(self.root, width=10, borderwidth=5, justify="right", font=('Segoe 40 bold'))

        # Places entry box on window
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Creates number pad buttons
        button_1 = Button(self.root, text="1", padx=34, pady=15, command=lambda: self.entry.enter_numbers(1))
        button_2 = Button(self.root, text="2", padx=34, pady=15, command=lambda: self.entry.enter_numbers(2))
        button_3 = Button(self.root, text="3", padx=34, pady=15, command=lambda: self.entry.enter_numbers(3))
        button_4 = Button(self.root, text="4", padx=34, pady=15, command=lambda: self.entry.enter_numbers(4))
        button_5 = Button(self.root, text="5", padx=34, pady=15, command=lambda: self.entry.enter_numbers(5))
        button_6 = Button(self.root, text="6", padx=34, pady=15, command=lambda: self.entry.enter_numbers(6))
        button_7 = Button(self.root, text="7", padx=34, pady=15, command=lambda: self.entry.enter_numbers(7))
        button_8 = Button(self.root, text="8", padx=34, pady=15, command=lambda: self.entry.enter_numbers(8))
        button_9 = Button(self.root, text="9", padx=34, pady=15, command=lambda: self.entry.enter_numbers(9))
        button_0 = Button(self.root, text="0", padx=34, pady=15, command=lambda: self.entry.enter_numbers(0))

        # Creates buttons holding calculation functions and clear function
        button_add = Button(self.root, text="+", padx=34, pady=15, command=lambda: self.entry.operation("+"))
        button_subtract = Button(self.root, text="-", padx=34, pady=15, command=lambda: self.entry.operation("-"))
        button_multiply = Button(self.root, text="*", padx=34, pady=15, command=lambda: self.entry.operation("*"))
        button_divide = Button(self.root, text="/", padx=34, pady=15, command=lambda: self.entry.operation("/"))
        button_percent = Button(self.root, text="%", padx=34, pady=15, command=self.entry.find_percent)
        button_equal = Button(self.root, text="=", padx=34, pady=15, command=self.entry.calculate)
        button_clear = Button(self.root, text="CE", padx=34, pady=15, command=self.entry.clear_entry)
        button_clear_all = Button(self.root, text="C", padx=34, pady=15, command=self.entry.clear_all)
        button_backspace = Button(self.root, text="BKSP", padx=34, pady=15, command=self.entry.backspace)
        button_fraction = Button(self.root, text="1/X", padx=34, pady=15, command=self.entry.fraction)
        button_exponent = Button(self.root, text="x^2", padx=34, pady=15, command=self.entry.exponent)
        button_square_root = Button(self.root, text="√x", padx=34, pady=15, command=self.entry.square_root)
        button_pos_neg = Button(self.root, text="+/-", padx=34, pady=15, command=self.entry.pos_neg)
        button_decimal = Button(self.root, text=".", padx=34, pady=15, command=self.entry.add_decimal)

        # Adds buttons to grid
        # First row of buttons after entry box - Contains buttons %, CE, C, BKSP
        button_percent.grid(row=1, column=0, sticky="nsew")
        button_clear.grid(row=1, column=1, sticky="nsew")
        button_clear_all.grid(row=1, column=2, sticky="nsew")
        button_backspace.grid(row=1, column=3, sticky="nsew")

        # Second row of buttons - Contains buttons 1/X, X^2, √x, /
        button_fraction.grid(row=2, column=0, sticky="nsew")
        button_exponent.grid(row=2, column=1, sticky="nsew")
        button_square_root.grid(row=2, column=2, sticky="nsew")
        button_divide.grid(row=2, column=3, sticky="nsew")

        # Third row of buttons - Contains 7, 8, 9, X
        button_7.grid(row=3, column=0, sticky="nsew")
        button_8.grid(row=3, column=1, sticky="nsew")
        button_9.grid(row=3, column=2, sticky="nsew")
        button_multiply.grid(row=3, column=3, sticky="nsew")
        
        # Fourth row of buttons - Contains 4, 5, 6, -
        button_4.grid(row=4, column=0, sticky="nsew")
        button_5.grid(row=4, column=1, sticky="nsew")
        button_6.grid(row=4, column=2, sticky="nsew")
        button_subtract.grid(row=4, column=3, sticky="nsew")

        # Fifth row of buttons - Contains 1, 2, 3, +
        button_1.grid(row=5, column=0, sticky="nsew")
        button_2.grid(row=5, column=1, sticky="nsew")
        button_3.grid(row=5, column=2, sticky="nsew")
        button_add.grid(row=5, column=3, sticky="nsew")

        # Final row of buttons - Contains +/-, 0, ., =
        button_pos_neg.grid(row=6, column=0, sticky="nsew")
        button_0.grid(row=6, column=1, sticky="nsew")
        button_decimal.grid(row=6, column=2, sticky="nsew")
        button_equal.grid(row=6, column=3, sticky="nsew")

        # Maintains application loop until retrieving input to close application
        self.root.mainloop()

new_calculator = Calculator()
