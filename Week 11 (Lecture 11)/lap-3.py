import tkinter as tk

def login(event=None):
    user = entry_user.get()
    pwd = entry_pass.get()
    if not user or not pwd:
        status_label.config(text="Fields cannot be empty", fg="red")
    else:
        status_label.config(text="Login successful", fg="green")

def clear_form(event=None):
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)
    status_label.config(text="")

def focus_in(event, field_name):
    status_label.config(text=f"{field_name} is active", fg="blue")

def focus_out(event):
    status_label.config(text="")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x250")

tk.Label(root, text="Username:").pack(pady=5)
entry_user = tk.Entry(root)
entry_user.pack()
entry_user.bind("<FocusIn>", lambda e: focus_in(e, "Username"))
entry_user.bind("<FocusOut>", focus_out)

tk.Label(root, text="Password:").pack(pady=5)
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()
entry_pass.bind("<FocusIn>", lambda e: focus_in(e, "Password"))
entry_pass.bind("<FocusOut>", focus_out)

tk.Button(root, text="Login", command=login).pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack()

root.bind("<Return>", login)
root.bind("<Escape>", clear_form)

root.mainloop()