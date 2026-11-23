import tkinter as tk
from tkinter import messagebox

def save_data():
    student_id = entry_id.get()
    name = entry_name.get()
    if not student_id or not name:
        status_label.config(text="ID and Name are required", fg="red")
        return
    status_label.config(text="Saved successfully", fg="green")
    print(f"Saved: {student_id}, {name}")

def clear_data():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_dept.delete(0, tk.END)
    entry_sem.delete(0, tk.END)
    text_notes.delete("1.0", tk.END)
    status_label.config(text="")

root = tk.Tk()
root.title("Student Registration GUI")
root.geometry("500x600")

header_frame = tk.Frame(root, bg="darkblue")
header_frame.pack(fill="x")
tk.Label(header_frame, text="Student Registration", font=("Arial", 16, "bold"), bg="darkblue", fg="white").pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(fill="both", expand=True, padx=20, pady=10)

tk.Label(form_frame, text="Personal Information", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=5)

tk.Label(form_frame, text="Student ID:").grid(row=1, column=0, sticky="w", pady=2)
entry_id = tk.Entry(form_frame)
entry_id.grid(row=1, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Full Name:").grid(row=2, column=0, sticky="w", pady=2)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=2, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Email:").grid(row=3, column=0, sticky="w", pady=2)
entry_email = tk.Entry(form_frame)
entry_email.grid(row=3, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Phone:").grid(row=4, column=0, sticky="w", pady=2)
entry_phone = tk.Entry(form_frame)
entry_phone.grid(row=4, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Academic Information", font=("Arial", 12, "bold")).grid(row=5, column=0, columnspan=2, sticky="w", pady=10)

tk.Label(form_frame, text="Department:").grid(row=6, column=0, sticky="w", pady=2)
entry_dept = tk.Entry(form_frame)
entry_dept.grid(row=6, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Semester:").grid(row=7, column=0, sticky="w", pady=2)
entry_sem = tk.Entry(form_frame)
entry_sem.grid(row=7, column=1, sticky="ew", pady=2)

tk.Label(form_frame, text="Notes:").grid(row=8, column=0, sticky="nw", pady=5)
text_notes = tk.Text(form_frame, height=4)
text_notes.grid(row=8, column=1, sticky="ew", pady=5)

form_frame.columnconfigure(1, weight=1)

action_frame = tk.Frame(root)
action_frame.pack(fill="x", padx=20, pady=10)

tk.Button(action_frame, text="Save", command=save_data).pack(side="left", padx=5)
tk.Button(action_frame, text="Clear", command=clear_data).pack(side="left", padx=5)
tk.Button(action_frame, text="Exit", command=root.destroy).pack(side="right", padx=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()