import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.resizable(0, 0)

        # Entry widget with color scheme
        self.entry = tk.Entry(master, width=35, bg='#DDF2FD', fg='black', borderwidth=5, justify='right', font='Calibri 15')
        self.entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12)

        self.create_buttons()

    def create_buttons(self):
        # Buttons configuration
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('x', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('AC', 4, 3)
        ]

        # Create and place buttons on the grid
        for (text, row, col) in buttons:
            command = self.get_command(text)
            button = tk.Button(self.master, text=text, padx=20, pady=20, command=command, font='Calibri 12', bg='#427D9D', fg='white')
            button.grid(row=row, column=col, sticky="nsew")

        # Configure row and column weights for uniform sizing
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)
            self.master.grid_rowconfigure(i, weight=1)

    def get_command(self, text):
        # Determine the command based on the button text
        if text.isdigit() or text == '.':
            return lambda: self.button_click(text)
        elif text == 'AC':
            return self.button_clear
        elif text == '=':
            return self.button_equal
        else:
            return lambda: self.button_get(text)

    def button_click(self, number):
        # Handles number and decimal point button click
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, current + number)

    def button_clear(self):
        # Clears the entry field
        self.entry.delete(0, tk.END)

    def button_get(self, operator):
        # Handles operator button click
        self.first_number = self.entry.get()
        self.operation = operator
        self.entry.delete(0, tk.END)

    def button_equal(self):
        # Handles the equal button click
        try:
            second_number = self.entry.get()
            result = self.calculate_result(second_number)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, result)
        except ZeroDivisionError:
            self.entry.insert(0, 'Error')

    def calculate_result(self, second_number):
        # Perform the calculation based on the operation
        if self.operation == '+':
            return float(self.first_number) + float(second_number)
        elif self.operation == '-':
            return float(self.first_number) - float(second_number)
        elif self.operation == 'x':
            return float(self.first_number) * float(second_number)
        elif self.operation == '/':
            return float(self.first_number) / float(second_number)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
