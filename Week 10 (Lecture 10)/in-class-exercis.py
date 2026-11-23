import tkinter as tk

def show_message(text):
    status.config(text=text)
    root.after(
        3000,
        lambda: status.config(text="Ready")
    )

root = tk.Tk()
root.title("Status Bar Challenge")
root.geometry("300x200")

status = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status.pack(side=tk.BOTTOM, fill=tk.X)

btn = tk.Button(root, text="Save", command=lambda: show_message("Student saved successfully"))
btn.pack(pady=50)

root.mainloop()