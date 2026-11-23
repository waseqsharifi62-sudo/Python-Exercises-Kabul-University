import tkinter as tk
from tkinter import ttk

def update_count(event):
    count = len(listbox.curselection())
    count_label.config(text=f"Selected Courses: {count}")

def show_selection():
    selected_indices = listbox.curselection()
    selected_courses = [listbox.get(i) for i in selected_indices]
    semester = combo_sem.get()
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, f"Semester: {semester}\nCourses:\n")
    for course in selected_courses:
        text_output.insert(tk.END, f"- {course}\n")

def clear_selection():
    listbox.selection_clear(0, tk.END)
    text_output.delete("1.0", tk.END)
    count_label.config(text="Selected Courses: 0")

root = tk.Tk()
root.title("Course Selection")
root.geometry("400x500")

courses = ["Math", "Physics", "Chemistry", "Biology", "Computer Science", "History", "Geography", "Literature", "Art", "Music", "Economics", "Philosophy"]

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=20, pady=10)

scrollbar = tk.Scrollbar(frame, orient="vertical")
listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

scrollbar.pack(side="right", fill="y")
listbox.pack(side="left", fill="both", expand=True)

for course in courses:
    listbox.insert(tk.END, course)

listbox.bind("<<ListboxSelect>>", update_count)

count_label = tk.Label(root, text="Selected Courses: 0")
count_label.pack()

tk.Label(root, text="Semester").pack(pady=5)
combo_sem = ttk.Combobox(root, values=["Fall", "Spring", "Summer"])
combo_sem.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)
tk.Button(btn_frame, text="Show Selection", command=show_selection).pack(side="left", padx=5)
tk.Button(btn_frame, text="Clear", command=clear_selection).pack(side="left", padx=5)

text_output = tk.Text(root, height=5)
text_output.pack(fill="both", padx=20, pady=10)

root.mainloop()