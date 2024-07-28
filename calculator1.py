import tkinter as tk
from tkinter import messagebox

# Function to update the display
def update_display(value):
    current = display_var.get()
    display_var.set(current + value)

# Function to clear the display
def clear_display():
    display_var.set("")

# Function to perform the calculation
def calculate():
    try:
        expression = display_var.get()
        result = eval(expression)  # Note: Using eval can be risky; consider safer alternatives
        display_var.set(str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input.")
        display_var.set("")

# Function to handle button hover effect
def on_enter(e):
    e.widget['bg'] = '#ccc'

def on_leave(e):
    e.widget['bg'] = '#eee'

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")
root.configure(bg='#333')
root.resizable(False, False)

# Display
display_var = tk.StringVar()
display = tk.Entry(root, textvariable=display_var, font=('Arial', 24), bg='#eee', relief='flat', justify='right')
display.pack(pady=20, padx=10, fill='x')

# Styles
button_style = {'font': ('Arial', 18), 'bg': '#eee', 'fg': '#333', 'relief': 'flat', 'bd': 0, 'width': 4, 'height': 2}
operator_button_style = {'font': ('Arial', 18), 'bg': '#f0a500', 'fg': 'black', 'relief': 'flat', 'bd': 0, 'width': 4, 'height': 2}

# Frame for buttons
buttons_frame = tk.Frame(root, bg='#333')
buttons_frame.pack()

# Number buttons
numbers = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1)
]
for (text, row, col) in numbers:
    button = tk.Button(buttons_frame, text=text, command=lambda t=text: update_display(t), **button_style)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Operator buttons
operators = [
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 0), ('=', 4, 2)
]
for (text, row, col) in operators:
    if text == '=':
        button = tk.Button(buttons_frame, text=text, command=calculate, **operator_button_style)
    elif text == 'C':
        button = tk.Button(buttons_frame, text=text, command=clear_display, **operator_button_style)
    else:
        button = tk.Button(buttons_frame, text=text, command=lambda t=text: update_display(t), **operator_button_style)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Enter>", on_enter)
    button.bind("<Leave>", on_leave)

# Run the application
root.mainloop()
