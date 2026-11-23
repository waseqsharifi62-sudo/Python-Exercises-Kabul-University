import tkinter as tk
from tkinter import ttk

def save_settings():
    summary = f"Email: {var_email.get()}\nSMS: {var_sms.get()}\nDesktop: {var_desktop.get()}\nTheme: {var_theme.get()}\nVolume: {var_volume.get()}\nLanguage: {var_lang.get()}"
    text_summary.delete("1.0", tk.END)
    text_summary.insert(tk.END, summary)

def reset_settings():
    var_email.set(0)
    var_sms.set(0)
    var_desktop.set(0)
    var_theme.set("Light")
    var_volume.set(50)
    var_lang.set("English")
    text_summary.delete("1.0", tk.END)

root = tk.Tk()
root.title("Settings Panel")
root.geometry("400x500")

var_email = tk.IntVar()
var_sms = tk.IntVar()
var_desktop = tk.IntVar()
var_theme = tk.StringVar(value="Light")
var_volume = tk.IntVar(value=50)
var_lang = tk.StringVar(value="English")

tk.Label(root, text="Notifications").pack(anchor="w", padx=20, pady=(10, 0))
tk.Checkbutton(root, text="Email", variable=var_email).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="SMS", variable=var_sms).pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Desktop", variable=var_desktop).pack(anchor="w", padx=30)

tk.Label(root, text="Theme").pack(anchor="w", padx=20, pady=(10, 0))
tk.Radiobutton(root, text="Light", variable=var_theme, value="Light").pack(anchor="w", padx=30)
tk.Radiobutton(root, text="Dark", variable=var_theme, value="Dark").pack(anchor="w", padx=30)
tk.Radiobutton(root, text="System", variable=var_theme, value="System").pack(anchor="w", padx=30)

tk.Label(root, text="Notification Volume").pack(anchor="w", padx=20, pady=(10, 0))
tk.Scale(root, from_=0, to=100, orient="horizontal", variable=var_volume).pack(fill="x", padx=30)

tk.Label(root, text="Language").pack(anchor="w", padx=20, pady=(10, 0))
ttk.Combobox(root, textvariable=var_lang, values=["English", "Spanish", "French", "German"]).pack(fill="x", padx=30)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Save", command=save_settings).pack(side="left", padx=5)
tk.Button(btn_frame, text="Reset", command=reset_settings).pack(side="left", padx=5)

text_summary = tk.Text(root, height=8)
text_summary.pack(fill="both", expand=True, padx=20, pady=10)

root.mainloop()