import tkinter as tk
from tkinter import ttk

def validate_and_display():
    name = entry_name.get()
    if not name:
        summary_label.config(text="Name is required", fg="red")
        return
    
    dept = combo_dept.get()
    mode = var_mode.get()
    
    comms = []
    if var_email.get(): comms.append("Email")
    if var_sms.get(): comms.append("SMS")
    
    exp = scale_exp.get()
    
    selected_skills = [listbox_skills.get(i) for i in listbox_skills.curselection()]
    
    summary = f"Name: {name}\nDept: {dept}\nMode: {mode}\nComms: {', '.join(comms)}\nExperience: {exp}\nSkills: {', '.join(selected_skills)}"
    summary_label.config(text=summary, fg="black")

root = tk.Tk()
root.title("Student Preferences")
root.geometry("400x600")

frame_personal = ttk.LabelFrame(root, text="Personal Info")
frame_personal.pack(fill="x", padx=10, pady=5)

tk.Label(frame_personal, text="Name:").grid(row=0, column=0, sticky="w")
entry_name = tk.Entry(frame_personal)
entry_name.grid(row=0, column=1, sticky="ew")

tk.Label(frame_personal, text="Department:").grid(row=1, column=0, sticky="w")
combo_dept = ttk.Combobox(frame_personal, values=["CS", "Math", "Physics"])
combo_dept.grid(row=1, column=1, sticky="ew")
frame_personal.columnconfigure(1, weight=1)

frame_study = ttk.LabelFrame(root, text="Study Mode")
frame_study.pack(fill="x", padx=10, pady=5)

var_mode = tk.StringVar(value="Full-time")
tk.Radiobutton(frame_study, text="Full-time", variable=var_mode, value="Full-time").pack(anchor="w")
tk.Radiobutton(frame_study, text="Part-time", variable=var_mode, value="Part-time").pack(anchor="w")

frame_comms = ttk.LabelFrame(root, text="Communication")
frame_comms.pack(fill="x", padx=10, pady=5)

var_email = tk.IntVar()
var_sms = tk.IntVar()
tk.Checkbutton(frame_comms, text="Email", variable=var_email).pack(anchor="w")
tk.Checkbutton(frame_comms, text="SMS", variable=var_sms).pack(anchor="w")

frame_exp = ttk.LabelFrame(root, text="Experience")
frame_exp.pack(fill="x", padx=10, pady=5)

scale_exp = tk.Scale(frame_exp, from_=1, to=10, orient="horizontal")
scale_exp.pack(fill="x")

frame_skills = ttk.LabelFrame(root, text="Skills")
frame_skills.pack(fill="both", expand=True, padx=10, pady=5)

listbox_skills = tk.Listbox(frame_skills, selectmode=tk.MULTIPLE, height=4)
listbox_skills.pack(fill="both", expand=True)
for s in ["Python", "Java", "C++", "Data Analysis", "Web Dev"]:
    listbox_skills.insert(tk.END, s)

tk.Button(root, text="Validate & Display", command=validate_and_display).pack(pady=5)

summary_label = tk.Label(root, text="", justify="left")
summary_label.pack(pady=5)

root.mainloop()