import tkinter as tk

def on_key_press(event):
    key_label.config(text=f"Key: {event.keysym} | Char: {event.char}")

def on_escape(event):
    key_label.config(text="")

def on_ctrl_s(event):
    status_label.config(text="Saved")

root = tk.Tk()
root.title("Keyboard Event Viewer")
root.geometry("400x300")

key_label = tk.Label(root, text="Press a key", font=("Arial", 14))
key_label.pack(pady=20)

status_label = tk.Label(root, text="", fg="green")
status_label.pack()

entry = tk.Entry(root)
entry.pack(pady=20)

root.bind("<KeyPress>", on_key_press)
root.bind("<Escape>", on_escape)
root.bind("<Control-s>", on_ctrl_s)

root.mainloop()