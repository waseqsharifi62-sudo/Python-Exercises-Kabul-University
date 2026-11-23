import tkinter as tk

root = tk.Tk()
root.geometry('500x400')

header = tk.Frame(root, bg='grey', height=60)
header.pack(fill='x')

footer = tk.Frame(root, bg='grey', height=60)
footer.pack(side='bottom', fill='x')

content = tk.Frame(root)
content.pack(fill='both', expand=True, padx=10, pady=10)

content.columnconfigure(1, weight=1)

tk.Label(content, text='Enter Text:').grid(row=0, column=0, sticky='w', padx=5, pady=5)
entry = tk.Entry(content)
entry.grid(row=0, column=1, sticky='ew', padx=5, pady=5)

root.mainloop()