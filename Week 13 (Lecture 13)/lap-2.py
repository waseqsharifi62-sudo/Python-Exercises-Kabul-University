import tkinter as tk

def move(event):
    x1, y1, x2, y2 = canvas.coords(player)
    speed = 15 if event.state & 0x0001 else 5
    new_x1, new_y1, new_x2, new_y2 = x1, y1, x2, y2

    if event.keysym == "Up":
        new_y1 -= speed
        new_y2 -= speed
    elif event.keysym == "Down":
        new_y1 += speed
        new_y2 += speed
    elif event.keysym == "Left":
        new_x1 -= speed
        new_x2 -= speed
    elif event.keysym == "Right":
        new_x1 += speed
        new_x2 += speed

    if new_x1 >= 0 and new_x2 <= canvas.winfo_width() and new_y1 >= 0 and new_y2 <= canvas.winfo_height():
        canvas.coords(player, new_x1, new_y1, new_x2, new_y2)
        coord_label.config(text=f"X: {int(new_x1)}, Y: {int(new_y1)}")

def reset(event):
    canvas.coords(player, 175, 175, 225, 225)
    coord_label.config(text="X: 175, Y: 175")

root = tk.Tk()
root.title("Keyboard Player")
root.geometry("400x400")

coord_label = tk.Label(root, text="X: 175, Y: 175")
coord_label.pack(pady=5)

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

player = canvas.create_oval(175, 175, 225, 225, fill="blue")

root.bind("<Key>", move)
root.bind("<r>", reset)

canvas.focus_set()
root.mainloop()