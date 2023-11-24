import tkinter as tk

def handle_button_click(button):
    current_input = input_var.get()

    if button == 'C':
        input_var.set('')
    elif button == '=':
        try:
            result = str(eval(current_input))
            input_var.set(result)
        except Exception as e:
            input_var.set('Error')
    else:
        input_var.set(current_input + button)

# Create the main window
calculator_window = tk.Tk()
calculator_window.title("Calculator")

# Entry widget for display
input_var = tk.StringVar()
input_entry = tk.Entry(calculator_window, textvariable=input_var, width=16, font=('Arial', 20), justify='right')
input_entry.grid(row=0, column=0, columnspan=4)

# Define button positions and labels
button_data = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons in a grid
for (text, row, col) in button_data:
    button = tk.Button(calculator_window, text=text, width=4, height=2, font=('Arial', 16),
                       command=lambda t=text: handle_button_click(t))
    button.grid(row=row, column=col)

# Start the main event loop
calculator_window.mainloop()
