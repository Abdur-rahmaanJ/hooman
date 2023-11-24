import tkinter as tk

def on_click(button):
    current_text = entry.get()

    if button == 'C':
        entry.delete(0, tk.END)
    elif button == '=':
        try:
            result = str(eval(current_text))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, 'Error')
    else:
        entry.insert(tk.END, button)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Entry widget for display
entry = tk.Entry(root, width=16, font=('Arial', 20), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define button positions and labels
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons in a grid
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=4, height=2, font=('Arial', 16),
                       command=lambda t=text: on_click(t))
    button.grid(row=row, column=col)

# Start the main event loop
root.mainloop()
