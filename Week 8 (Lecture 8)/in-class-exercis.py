import tkinter as tk

def check_validity(*args):
    if entry_name.get() and entry_email.get() and entry_subject.get() and text_message.get("1.0", tk.END).strip():
        btn_send.config(state="normal")
    else:
        btn_send.config(state="disabled")

def send_form():
    print("Message sent")
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_subject.delete(0, tk.END)
    text_message.delete("1.0", tk.END)

def clear_form():
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_subject.delete(0, tk.END)
    text_message.delete("1.0", tk.END)

root = tk.Tk()
root.title("Contact Form")
root.geometry("400x500")

header_frame = tk.Frame(root, bg="lightgreen")
header_frame.pack(fill="x")
tk.Label(header_frame, text="Contact Us", font=("Arial", 16, "bold"), bg="lightgreen").pack(pady=10)

form_frame = tk.Frame(root)
form_frame.pack(fill="both", expand=True, padx=20, pady=10)

tk.Label(form_frame, text="Name:").grid(row=0, column=0, sticky="w", pady=5)
entry_name = tk.Entry(form_frame)
entry_name.grid(row=0, column=1, sticky="ew", pady=5)
entry_name.bind("<KeyRelease>", check_validity)

tk.Label(form_frame, text="Email:").grid(row=1, column=0, sticky="w", pady=5)
entry_email = tk.Entry(form_frame)
entry_email.grid(row=1, column=1, sticky="ew", pady=5)
entry_email.bind("<KeyRelease>", check_validity)

tk.Label(form_frame, text="Subject:").grid(row=2, column=0, sticky="w", pady=5)
entry_subject = tk.Entry(form_frame)
entry_subject.grid(row=2, column=1, sticky="ew", pady=5)
entry_subject.bind("<KeyRelease>", check_validity)

tk.Label(form_frame, text="Message:").grid(row=3, column=0, sticky="nw", pady=5)
text_message = tk.Text(form_frame, height=5)
text_message.grid(row=3, column=1, sticky="ew", pady=5)
text_message.bind("<KeyRelease>", check_validity)

form_frame.columnconfigure(1, weight=1)

action_frame = tk.Frame(root)
action_frame.pack(fill="x", padx=20, pady=10)

btn_send = tk.Button(action_frame, text="Send", state="disabled", command=send_form)
btn_send.pack(side="left", padx=5)
tk.Button(action_frame, text="Clear", command=clear_form).pack(side="left", padx=5)

root.mainloop()