import tkinter as tk
from tkinter import messagebox

def submit(event=None):
    show_status("Submitted successfully")

def save(event=None):
    show_status("Data saved")

def clear(event=None):
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    text_address.delete("1.0", tk.END)
    show_status("Form cleared")

def validate(event):
    widget = event.widget
    if not widget.get():
        widget.config(bg="pink")
    else:
        widget.config(bg="white")

def on_click(event):
    show_status("Mouse clicked on window")

def show_status(msg):
    status_label.config(text=msg, fg="blue")
    root.after(3000, lambda: status_label.config(text=""))

def on_close():
    root.destroy()

root = tk.Tk()
root.title("Student Registration")
root.geometry("400x500")
root.protocol("WM_DELETE_WINDOW", on_close)

tk.Label(root, text="Student ID:").pack(anchor="w", padx=20)
entry_id = tk.Entry(root)
entry_id.pack(fill="x", padx=20)
entry_id.bind("<FocusOut>", validate)
entry_id.bind("<FocusIn>", lambda e: show_status("Editing Student ID"))

tk.Label(root, text="Name:").pack(anchor="w", padx=20)
entry_name = tk.Entry(root)
entry_name.pack(fill="x", padx=20)
entry_name.bind("<FocusOut>", validate)
entry_name.bind("<FocusIn>", lambda e: show_status("Editing Name"))

tk.Label(root, text="Email:").pack(anchor="w", padx=20)
entry_email = tk.Entry(root)
entry_email.pack(fill="x", padx=20)
entry_email.bind("<FocusOut>", validate)

tk.Label(root, text="Phone:").pack(anchor="w", padx=20)
entry_phone = tk.Entry(root)
entry_phone.pack(fill="x", padx=20)
entry_phone.bind("<FocusOut>", validate)

tk.Label(root, text="Address:").pack(anchor="w", padx=20)
text_address = tk.Text(root, height=4)
text_address.pack(fill="x", padx=20)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Save", command=save).pack(side="left", padx=5)
tk.Button(btn_frame, text="Clear", command=clear).pack(side="left", padx=5)
tk.Button(btn_frame, text="Exit", command=on_close).pack(side="left", padx=5)

status_label = tk.Label(root, text="", bd=1, relief=tk.SUNKEN, anchor="w")
status_label.pack(side="bottom", fill="x")

root.bind("<Return>", submit)
root.bind("<Escape>", clear)
root.bind("<Control-s>", save)
root.bind("<Button-1>", on_click)

root.mainloop()