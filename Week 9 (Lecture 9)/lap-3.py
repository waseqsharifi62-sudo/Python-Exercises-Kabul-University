import tkinter as tk

def clear_text():
    text_editor.delete("1.0", tk.END)
    status_label.config(text="Cleared")

def insert_sample():
    text_editor.insert(tk.END, "This is a sample note.\n")
    status_label.config(text="Sample inserted")

def toggle_state():
    if str(text_editor.cget("state")) == "normal":
        text_editor.config(state="disabled")
        btn_toggle.config(text="Enable")
        status_label.config(text="Editor disabled")
    else:
        text_editor.config(state="normal")
        btn_toggle.config(text="Disable")
        status_label.config(text="Editor enabled")

root = tk.Tk()
root.title("Notes Editor")
root.geometry("500x400")

header_frame = tk.Frame(root, bg="lightblue")
header_frame.pack(fill="x")
tk.Label(header_frame, text="Notes Editor", font=("Arial", 14), bg="lightblue").pack(pady=10)

text_editor = tk.Text(root, wrap="word")
text_editor.pack(fill="both", expand=True, padx=10, pady=10)

action_frame = tk.Frame(root)
action_frame.pack(fill="x", padx=10, pady=5)

tk.Button(action_frame, text="Clear", command=clear_text).pack(side="left", padx=5)
tk.Button(action_frame, text="Insert Sample", command=insert_sample).pack(side="left", padx=5)
btn_toggle = tk.Button(action_frame, text="Disable", command=toggle_state)
btn_toggle.pack(side="left", padx=5)

status_label = tk.Label(root, text="Ready", fg="blue")
status_label.pack(pady=5)

root.mainloop()