import tkinter as tk

# Main window
root = tk.Tk()
root.title("Colorful Calculator")
root.configure(bg="#2e2e2e")  # dark gray background

# Entry field (display)
entry = tk.Entry(root, width=20, borderwidth=5, font=('Arial', 24),
                 justify='right', bg="#1e1e1e", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button functions
def button_click(value):
    entry.insert(tk.END, value)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def button_backspace():
    entry.delete(len(entry.get()) - 1, tk.END)

def keypress(event):
    char = event.char
    if char in '0123456789+-*/.=()':
        button_click(char)
    elif event.keysym == 'Return':
        button_equal()
    elif event.keysym == 'BackSpace':
        button_backspace()
    elif event.keysym == 'Escape':
        button_clear()

root.bind('<Key>', keypress)

# Button layout and styles
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('(', 5, 0), (')', 5, 1), ('=', 5, 2), ('←', 5, 3)
]

# Color palette
btn_bg = "#3e3e3e"
btn_fg = "white"
btn_highlight = "#ff7f50"  # coral
btn_clear = "#ff4c4c"

# Create buttons
for (text, row, col) in buttons:
    if text == 'C':
        command = button_clear
        bg = btn_clear
    elif text == '=':
        command = button_equal
        bg = btn_highlight
    elif text == '←':
        command = button_backspace
        bg = btn_bg
    else:
        command = lambda val=text: button_click(val)
        bg = btn_bg

    btn = tk.Button(root, text=text, padx=30, pady=20,
                    font=('Arial', 14), bg=bg, fg=btn_fg,
                    activebackground="#5e5e5e", activeforeground="white",
                    command=command)
    btn.grid(row=row, column=col, sticky="nsew")

# Responsive grid
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run app
root.mainloop()
