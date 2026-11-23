import tkinter as tk

def edit_profile():
    pass

root = tk.Tk()
root.title("Image Profile Card")
root.geometry("300x400")

card_frame = tk.Frame(root, borderwidth=2, relief="groove")
card_frame.pack(padx=20, pady=20, fill="both", expand=True)

img = tk.PhotoImage(width=100, height=100)
img.put("blue", to=(0, 0, 100, 100))

img_label = tk.Label(card_frame, image=img)
img_label.image = img
img_label.pack(pady=10)

tk.Label(card_frame, text="Ali Reza", font=("Helvetica", 16, "bold")).pack(pady=5)
tk.Label(card_frame, text="Computer Science", font=("Helvetica", 12)).pack(pady=2)
tk.Label(card_frame, text="ali@example.com", font=("Helvetica", 10)).pack(pady=2)

btn_frame = tk.Frame(card_frame)
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Edit", command=edit_profile).pack(side="left", padx=5)
tk.Button(btn_frame, text="Close", command=root.destroy).pack(side="left", padx=5)

root.mainloop()