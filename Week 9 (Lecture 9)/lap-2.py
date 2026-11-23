import tkinter as tk

def save_data():
    status_label.config(text="Data saved successfully")

def clear_data():
    entry_name.delete(0, tk.END)
    entry_id.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    text_address.delete("1.0", tk.END)
    status_label.config(text="")

root = tk.Tk()
root.title("Profile Form")
root.geometry("400x500")

header_frame = tk.Frame(root, bg="lightgray")
header_frame.pack(fill="x", pady=10)
tk.Label(header_frame, text="Profile Form", font=("Arial", 16, "bold"), bg="lightgray").pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(fill="both", expand=True, padx=20)

tk.Label(form_frame, text="Full Name:").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=0, column=1, sticky="ew", pady=5)

tk.Label(form_frame, text="Student ID:").grid(row=1, column=0, sticky="w", pady=5)
entry_id = tk.Entry(form_frame)
entry_id.grid(row=1, column=1, sticky="ew", pady=5)

tk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky="w", pady=5)
entry_email = tk.Entry(form_frame)
entry_email.grid(row=2, column=1, sticky="ew", pady=5)

tk.Label(form_frame, text="Phone:").grid(row=3, column=0, sticky="w", pady=5)
entry_phone = tk.Entry(form_frame)
entry_phone.grid(row=3, column=1, sticky="ew", pady=5)

tk.Label(form_frame, text="Address:").grid(row=4, column=0, sticky="nw", pady=5)
text_address = tk.Text(form_frame, height=5)
text_address.grid(row=4, column=1, sticky="ew", pady=5)

form_frame.columnconfigure(1, weight=1)

action_frame = tk.Frame(root)
action_frame.pack(fill="x", padx=20, pady=10)

tk.Button(action_frame, text="Save", command=save_data).pack(side="left", padx=5)
tk.Button(action_frame, text="Clear", command=clear_data).pack(side="left", padx=5)

status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=5)

root.mainloop()