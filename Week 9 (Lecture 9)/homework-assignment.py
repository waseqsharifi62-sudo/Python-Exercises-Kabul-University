import tkinter as tk
import csv

def validate_and_save():
    emp_id = entry_id.get()
    name = entry_name.get()
    if not emp_id or not name:
        status_label.config(text="ID and Name required", fg="red")
        return
    address = text_address.get("1.0", tk.END).strip()
    with open("employees.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([emp_id, name, entry_email.get(), entry_phone.get(), entry_pos.get(), address])
    status_label.config(text="Employee saved", fg="green")

def clear_form():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_pos.delete(0, tk.END)
    text_address.delete("1.0", tk.END)
    status_label.config(text="")

root = tk.Tk()
root.title("Employee Registration")
root.geometry("500x600")

header_frame = tk.Frame(root, bg="gray")
header_frame.pack(fill="x")
tk.Label(header_frame, text="Employee Registration", font=("Arial", 16, "bold"), bg="gray", fg="white").pack(pady=10)

img = tk.PhotoImage(width=50, height=50)
img.put("white", to=(0, 0, 50, 50))
img_label = tk.Label(header_frame, image=img, bg="gray")
img_label.image = img
img_label.pack(pady=5)

form_frame = tk.Frame(root)
form_frame.pack(fill="both", expand=True, padx=20, pady=10)

tk.Label(form_frame, text="Employee ID:").grid(row=0, column=0, sticky="w", pady=2)
entry_id = tk.Entry(form_frame)
entry_id.grid(row=0, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Name:").grid(row=1, column=0, sticky="w", pady=2)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=1, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Email:").grid(row=2, column=0, sticky="w", pady=2)
entry_email = tk.Entry(form_frame)
entry_email.grid(row=2, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Phone:").grid(row=3, column=0, sticky="w", pady=2)
entry_phone = tk.Entry(form_frame)
entry_phone.grid(row=3, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Position:").grid(row=4, column=0, sticky="w", pady=2)
entry_pos = tk.Entry(form_frame)
entry_pos.grid(row=4, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Address:").grid(row=5, column=0, sticky="nw", pady=2)
text_address = tk.Text(form_frame, height=4)
text_address.grid(row=5, column=1, sticky="ew", pady=2)

form_frame.columnconfigure(1, weight=1)

action_frame = tk.Frame(root)
action_frame.pack(fill="x", padx=20, pady=10)

tk.Button(action_frame, text="Save", command=validate_and_save).pack(side="left", padx=5)
tk.Button(action_frame, text="Clear", command=clear_form).pack(side="left", padx=5)
tk.Button(action_frame, text="Exit", command=root.destroy).pack(side="right", padx=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()