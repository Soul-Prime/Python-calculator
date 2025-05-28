import tkinter as tk

#  main window
root = tk.Tk()
root.title("Simple Calculator")

#  widget with the input and output
entry = tk.Entry(root, width=20, borderwidth=5, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

#  insert button value
def button_click(value):
    entry.insert(tk.END, value)

# clearing the entry
def button_clear():
    entry.delete(0, tk.END)

# evaluateing the expression
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button labels and grid
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

# Creating buttons
for (text, row, col, *span) in buttons:
    colspan = span[0] if span else 1
    if text == 'C':
        command = button_clear
    elif text == '=':
        command = button_equal
    else:
        command = lambda val=text: button_click(val)

    btn = tk.Button(root, text=text, padx=30, pady=20, font=('Arial', 14),
                    command=command)
    btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew")

# exmpand the buttons
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i % 4, weight=1)

# Run the app
root.mainloop()
