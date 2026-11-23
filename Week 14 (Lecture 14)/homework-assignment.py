import tkinter as tk
from tkinter import ttk

def toggle_controls():
    if var_enable.get():
        combo_freq.config(state="readonly")
        scale_vol.config(state="normal")
    else:
        combo_freq.config(state="disabled")
        scale_vol.config(state="disabled")
    update_status()

def update_status():
    status = f"Enabled: {bool(var_enable.get())}\nFreq: {var_freq.get()}\nVol: {var_vol.get()}"
    status_label.config(text=status)

def reset_defaults():
    var_enable.set(1)
    var_freq.set("Daily")
    var_vol.set(50)
    toggle_controls()

root = tk.Tk()
root.title("Dynamic Preferences")
root.geometry("300x400")

var_enable = tk.IntVar(value=1)
var_freq = tk.StringVar(value="Daily")
var_vol = tk.IntVar(value=50)

tk.Checkbutton(root, text="Enable Notifications", variable=var_enable, command=toggle_controls).pack(anchor="w", padx=20, pady=10)

tk.Label(root, text="Frequency").pack(anchor="w", padx=20)
combo_freq = ttk.Combobox(root, textvariable=var_freq, values=["Hourly", "Daily", "Weekly"], state="readonly")
combo_freq.pack(fill="x", padx=20, pady=5)
combo_freq.bind("<<ComboboxSelected>>", lambda e: update_status())

tk.Label(root, text="Volume").pack(anchor="w", padx=20)
scale_vol = tk.Scale(root, from_=0, to=100, orient="horizontal", variable=var_vol, command=lambda e: update_status())
scale_vol.pack(fill="x", padx=20, pady=5)

tk.Button(root, text="Reset", command=reset_defaults).pack(pady=20)

status_label = tk.Label(root, text="", justify="left", bg="lightgray", relief="sunken")
status_label.pack(fill="x", side="bottom")
update_status()

root.mainloop()