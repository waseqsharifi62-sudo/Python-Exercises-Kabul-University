import tkinter as tk

root = tk.Tk()
root.title('Simple Calculator')
root.geometry('300x400')

display = tk.Entry(root, font=('Arial', 18), justify='right')
display.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for text, row, col in buttons:
    tk.Button(root, text=text, font=('Arial', 14)).grid(row=row, column=col, sticky='nsew', padx=2, pady=2)

for i in range(4):
    root.columnconfigure(i, weight=1)
for i in range(1, 5):
    root.rowconfigure(i, weight=1)

root.mainloop()