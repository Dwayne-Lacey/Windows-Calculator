import os, sys
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
        self.config(state="readonly")

# Standard commands for normal number entry, calculations, and field clearing
    # Adds numbers to entry box
    def enter_numbers(self, number):
        self.config(state="normal")
        if self.value_totalled == True:
            self.clear_entry()
            self.config(state="normal")
            self.value_totalled = False
        self.insert(END, number)
        self.config(state="readonly")

    # Clears entry field
    def clear_entry(self):
        self.config(state="normal")
        self.delete(0, END)
        self.config(state="readonly")
        
    # Clear stored number and current text in entrybox
    def clear_all(self):
        self.config(state="normal")
        self.clear_entry()
        self.value_totalled = False
        self.current_value = None
        self.last_operator = None
        self.config(state="readonly")

    # Backspace button: Deletes only the last number currently entered into the entrybox
    def backspace(self):
        self.config(state="normal")
        num_characters = len(self.get())
        self.delete(num_characters - 1, END)
        self.config(state="readonly")

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
                if value != 0:
                    self.current_value /= value
                else:
                    print("ZeroDivisionError: Stored value reset to 0")
                    self.current_value = 0
        self.last_operator = operator
        self.config(state="normal")
        self.clear_entry()
        self.config(state="readonly")

    # Performs calculations when equal button is pressed
    def calculate(self):
        self.operation(self.last_operator)
        self.current_value = self.check_num_type(self.current_value)
        self.config(state="normal")
        self.insert(0, self.current_value)
        self.current_value = None
        self.value_totalled = True
        self.config(state="readonly")

    # Function to check what value to return from entry box
    def return_entry_number(self):
        self.config(state="normal")
        print(self.get())

        # Checks if value exists currently within entry box, defaults to 0 if value does not exist.
        if len(self.get()) == 0:
            value_to_return = 0
        else:
            value_to_return = self.check_num_type(self.get())
        self.config(state="readonly")
        return value_to_return

    # Checks if value is a float or an integer and returns value as corresponding type
    def check_num_type(self, value):
        self.config(state="normal")
        if float(value) // 1 == float(value):
            if self.get().count('.') > 0:
                split_float = self.get().split('.')
                value_to_return = int(split_float[0])
            else:
                value_to_return = int(value)
        else:
            value_to_return = float(value)
        self.config(state="readonly")
        return value_to_return



# Specialized functions to alter inputs or use special calculations on a value
    # Pos/Neg Input: Converts existing input in entry box from negative to positive or positive to negative
    def pos_neg(self):
        self.config(state="normal")
        if self.get()[0] == '-':
            self.delete(0, 1)
        else:
            self.insert(0, '-')
        self.config(state="readonly")

    # Decimal Input: Inputs a decimal point. Limit of only 1 decimal point
    def add_decimal(self):
        self.config(state="normal")
        if self.get().count('.') < 1:
            self.insert(END, '.')
            self.value_totalled = False
        self.config(state="readonly")

    # Special functions performing immediate calculations with only one number minimum
    # Can be executed with or without number stored in memory
    def special_functions(self, function):
        value = self.return_entry_number()
        self.config(state="normal")
        if value == 0:
            self.clear_all()
            self.insert(0, 0)
        else:

            # Executes the desired function based on input from button
            # Functions possible are Fraction 1/X, Exponent x^2, and Square Root  
            if function == "1/X":
                value = self.check_num_type(1 / value)
            elif function == "X^2":
                value = self.check_num_type(value ** 2)
            elif function == "sqrt":
                value = self.check_num_type(sqrt(value))
            
            # Checks to see if there's currently a stored value and performs calculation based on last operator clicked and new value from special function
            if self.current_value != None:
                self.operation(value)
            
            # If there isn't a stored value to perform a calculation on, return result of calculation to entry box
            else:
                self.clear_entry()
                self.config(state="normal")
                self.insert(0, value)
        self.value_totalled = True
        self.config(state="readonly")

    # Percent function: Requires number stored in memory and a second number, function multiplies first and second numbers and then divides the result by 100 to get what percent num2 percent of num1
    # Uses last operator stored to decide if result should be added/subtracted etc. to first number
    def find_percent(self):
        value = self.return_entry_number()
        self.config(state="normal")
        if self.current_value == None:
            self.clear_entry()
            self.insert(0, 0)
        else:
            percent_value = self.check_num_type((value * self.current_value) / 100)
            self.operation(self.last_operator, percent_value)
            
# Modified button to allow button background to change when being hovered over
class HoverButton(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs, activebackground="#464646", relief=FLAT, fg="White", activeforeground="White", padx=30)
        self.hover_bg = "#373737"
        self.default_bg = self['bg']
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self.hover_bg
    
    def on_leave(self, e):
        self['background'] = self.default_bg

# Main application
class Calculator:
    def __init__(self):

        # Builds main window
        self.root = Tk()
        self.root.configure(bg="#1F1F1F")

        # Adds title to window
        self.root.title("Calculator")

        # Icon found at <a target="_blank" href="https://icons8.com/icon/aqWDxhA3yiU1/calculator">Calculator</a> icon by <a target="_blank" href="https://icons8.com">Icons8</a>
        # calc.ico must be saved in same directory as application
        dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
        self.root.iconbitmap(dirname + '\calc.ico')

        # Creates entrybox
        self.entry = CalcEntry(self.root, width=10, borderwidth=0, justify="right", font=('Segoe 34 bold'), readonlybackground="#1F1F1F", background="#1F1F1F", fg="White")
        

        # Places entry box on window
        self.entry.grid(row=1, column=1, columnspan=8, padx=10, pady=30, sticky="nsew")

        # Creates spacing labels
        row_0_spacer = Label(self.root, background="#1F1F1F", pady=14)
        row_2_spacer = Canvas(self.root, background="#1F1F1F", width=1, height=1, highlightthickness=0)
        row_4_spacer = Canvas(self.root, background="#1F1F1F", width=1, height=2, highlightthickness=0)
        row_6_spacer = Canvas(self.root, background="#1F1F1F", width=1, height=2, highlightthickness=0)
        row_8_spacer = Canvas(self.root, background="#1F1F1F", width=1, height=2, highlightthickness=0)
        row_10_spacer = Canvas(self.root, background="#1F1F1F", width=1, height=2, highlightthickness=0)
        row_12_spacer = Canvas(self.root, background="#1F1F1F", width=1, height=2, highlightthickness=0)
        row_14_spacer = Canvas(self.root, background="#1F1F1F", width=1, height=2, highlightthickness=0)

        column_0_spacer = Canvas(self.root, background="#1F1F1F", width=2, height=1, highlightthickness=0)
        column_2_spacer = Canvas(self.root, background="#1F1F1F", width=2, height=1, highlightthickness=0)
        column_4_spacer = Canvas(self.root, background="#1F1F1F", width=2, height=1, highlightthickness=0)
        column_6_spacer = Canvas(self.root, background="#1F1F1F", width=2, height=1, highlightthickness=0)
        column_8_spacer = Canvas(self.root, background="#1F1F1F", width=2, height=1, highlightthickness=0)

        # Creates number pad buttons
        button_1 = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="1", pady=6, command=lambda: self.entry.enter_numbers(1))
        button_2 = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="2", pady=6, command=lambda: self.entry.enter_numbers(2))
        button_3 = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="3", pady=6, command=lambda: self.entry.enter_numbers(3))
        button_4 = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="4", pady=6, command=lambda: self.entry.enter_numbers(4))
        button_5 = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="5", pady=6, command=lambda: self.entry.enter_numbers(5))
        button_6 = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="6", pady=6, command=lambda: self.entry.enter_numbers(6))
        button_7 = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="7", pady=3, command=lambda: self.entry.enter_numbers(7))
        button_8 = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="8", pady=3, command=lambda: self.entry.enter_numbers(8))
        button_9 = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="9", pady=3, command=lambda: self.entry.enter_numbers(9))
        button_0 = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="0", pady=6, command=lambda: self.entry.enter_numbers(0))

        # Creates buttons holding calculation functions and clear function
        button_add = HoverButton(self.root, background="#131313", font=('Segoe 18'), text="+", pady=6, command=lambda: self.entry.operation("+"))
        button_subtract = HoverButton(self.root, background="#131313", font=('Segoe 18'), text="−", pady=6, command=lambda: self.entry.operation("-"))
        button_multiply = HoverButton(self.root, background="#131313", font=('Segoe 20'), text="×", pady=3, command=lambda: self.entry.operation("*"))
        button_divide = HoverButton(self.root, background="#131313", font=('Segoe 20'), text="÷", pady=1, command=lambda: self.entry.operation("/"))
        button_percent = HoverButton(self.root, background="#131313", font=('Segoe 12'), text="%", pady=13, command=self.entry.find_percent)
        button_equal = HoverButton(self.root, background="#31302F", font=('Segoe 18'), text="=", pady=6, command=self.entry.calculate)
        button_clear = HoverButton(self.root, background="#131313", font=('Segoe 10'), text="CE", pady=13, command=self.entry.clear_entry)
        button_clear_all = HoverButton(self.root, background="#131313", font=('Segoe 10'), text="C", pady=13, command=self.entry.clear_all)
        button_backspace = HoverButton(self.root, background="#131313", font=('Segoe 12'), text="⌫", pady=13, command=self.entry.backspace)
        button_fraction = HoverButton(self.root, background="#131313", font=('Segoe 12'), text="¹/𝑥", pady=1, command=lambda: self.entry.special_functions("1/X"))
        button_exponent = HoverButton(self.root, background="#131313", font=('Segoe 12'), text="X²", pady=1, command=lambda: self.entry.special_functions("X^2"))
        button_square_root = HoverButton(self.root, background="#131313", font=('Segoe 12'), text="√x", pady=1, command=lambda: self.entry.special_functions("sqrt"))

        button_pos_neg = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text="+/-", pady=6, command=self.entry.pos_neg)
        button_decimal = HoverButton(self.root, background="#060606", font=('Segoe 12 bold'), text=".", pady=6, command=self.entry.add_decimal)

        # Adds buttons to grid
        # First row of buttons after entry box - Contains buttons %, CE, C, BKSP
        button_percent.grid(row=3, column=1, sticky="nsew")
        button_clear.grid(row=3, column=3, sticky="nsew")
        button_clear_all.grid(row=3, column=5, sticky="nsew")
        button_backspace.grid(row=3, column=7, sticky="nsew")

        # Second row of buttons - Contains buttons 1/X, X^2, √x, /
        button_fraction.grid(row=5, column=1, sticky="nsew")
        button_exponent.grid(row=5, column=3, sticky="nsew")
        button_square_root.grid(row=5, column=5, sticky="nsew")
        button_divide.grid(row=5, column=7, sticky="nsew")

        # Third row of buttons - Contains 7, 8, 9, X
        button_7.grid(row=7, column=1, sticky="nsew")
        button_8.grid(row=7, column=3, sticky="nsew")
        button_9.grid(row=7, column=5, sticky="nsew")
        button_multiply.grid(row=7, column=7, sticky="nsew")
        
        # Fourth row of buttons - Contains 4, 5, 6, -
        button_4.grid(row=9, column=1, sticky="nsew")
        button_5.grid(row=9, column=3, sticky="nsew")
        button_6.grid(row=9, column=5, sticky="nsew")
        button_subtract.grid(row=9, column=7, sticky="nsew")

        # Fifth row of buttons - Contains 1, 2, 3, +
        button_1.grid(row=11, column=1, sticky="nsew")
        button_2.grid(row=11, column=3, sticky="nsew")
        button_3.grid(row=11, column=5, sticky="nsew")
        button_add.grid(row=11, column=7, sticky="nsew")

        # Final row of buttons - Contains +/-, 0, ., =
        button_pos_neg.grid(row=13, column=1, sticky="nsew")
        button_0.grid(row=13, column=3, sticky="nsew")
        button_decimal.grid(row=13, column=5, sticky="nsew")
        button_equal.grid(row=13, column=7, sticky="nsew")

        # Adds spacing labels
        row_0_spacer.grid(row=0, column=0, columnspan=4)
        row_2_spacer.grid(row=2, column=0, columnspan=4)
        row_4_spacer.grid(row=4, column=0, columnspan=4)
        row_6_spacer.grid(row=6, column=0, columnspan=4)
        row_8_spacer.grid(row=8, column=0, columnspan=4)
        row_10_spacer.grid(row=10, column=0, columnspan=4)
        row_12_spacer.grid(row=12, column=0, columnspan=4)
        row_14_spacer.grid(row=14, column=0, columnspan=4)

        column_0_spacer.grid(row=0, column=0, sticky="ew")
        column_2_spacer.grid(row=4, column=2, sticky="ew")
        column_4_spacer.grid(row=4, column=4, sticky="ew")
        column_6_spacer.grid(row=4, column=6, sticky="ew")
        column_8_spacer.grid(row=0, column=8, sticky="ew")

        # Maintains application loop until retrieving input to close application
        self.root.mainloop()

new_calculator = Calculator()
