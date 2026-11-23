import tkinter as tk

def validate_focus_out(event):
    if not event.widget.get():
        status_label.config(text="Required field empty", fg="red")
    else:
        status_label.config(text="")

def submit_form(event=None):
    show_message("Form submitted")
    root.focus_set()

def save_form(event=None):
    show_message("Saved")

def clear_form(event=None):
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    status_label.config(text="Cleared")

def show_message(msg):
    status_label.config(text=msg, fg="green")
    root.after(2000, lambda: status_label.config(text=""))

def on_close():
    root.destroy()

root = tk.Tk()
root.title("Interactive Student Form")
root.geometry("350x300")
root.protocol("WM_DELETE_WINDOW", on_close)

tk.Label(root, text="Student ID:").pack(pady=5)
entry_id = tk.Entry(root)
entry_id.pack()
entry_id.bind("<FocusOut>", validate_focus_out)
entry_id.bind("<Return>", submit_form)

tk.Label(root, text="Full Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()
entry_name.bind("<FocusOut>", validate_focus_out)
entry_name.bind("<Return>", submit_form)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

tk.Button(root, text="Save", command=save_form).pack()

root.bind("<Control-s>", save_form)
root.bind("<Escape>", clear_form)

root.mainloop()