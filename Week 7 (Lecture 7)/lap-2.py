import tkinter as tk

def save_data():
    print(f"ID: {entry_id.get()}")
    print(f"Name: {entry_name.get()}")
    print(f"Department: {entry_dept.get()}")
    print(f"Semester: {entry_sem.get()}")

def clear_data():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_dept.delete(0, tk.END)
    entry_sem.delete(0, tk.END)

root = tk.Tk()
root.title('Student Registration')

form = tk.Frame(root, padx=20, pady=20)
form.pack(fill='both', expand=True)

tk.Label(form, text='Student ID:').grid(row=0, column=0, sticky='e', pady=5)
entry_id = tk.Entry(form)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(form, text='Name:').grid(row=1, column=0, sticky='e', pady=5)
entry_name = tk.Entry(form)
entry_name.grid(row=1, column=1, padx=10, pady=5)

tk.Label(form, text='Department:').grid(row=2, column=0, sticky='e', pady=5)
entry_dept = tk.Entry(form)
entry_dept.grid(row=2, column=1, padx=10, pady=5)

tk.Label(form, text='Semester:').grid(row=3, column=0, sticky='e', pady=5)
entry_sem = tk.Entry(form)
entry_sem.grid(row=3, column=1, padx=10, pady=5)

btn_frame = tk.Frame(form)
btn_frame.grid(row=4, column=0, columnspan=2, pady=20)
tk.Button(btn_frame, text='Save', command=save_data).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text='Clear', command=clear_data).pack(side=tk.LEFT, padx=5)

root.mainloop()