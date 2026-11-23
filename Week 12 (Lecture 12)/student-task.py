import tkinter as tk
import random

def move_player(event):
    x1, y1, x2, y2 = canvas.coords(player)
    speed = 10
    nx1, ny1, nx2, ny2 = x1, y1, x2, y2
    if event.keysym == "Up":
        ny1 -= speed; ny2 -= speed
    elif event.keysym == "Down":
        ny1 += speed; ny2 += speed
    elif event.keysym == "Left":
        nx1 -= speed; nx2 -= speed
    elif event.keysym == "Right":
        nx1 += speed; nx2 += speed

    if nx1 >= 0 and nx2 <= canvas.winfo_width() and ny1 >= 0 and ny2 <= canvas.winfo_height():
        canvas.coords(player, nx1, ny1, nx2, ny2)
        update_status()

def set_target(event):
    canvas.coords(target, event.x - 10, event.y - 10, event.x + 10, event.y + 10)

def start_auto():
    global running
    running = True
    animate_auto()

def animate_auto():
    global auto_dx, auto_dy, running
    if running:
        ax1, ay1, ax2, ay2 = canvas.coords(auto_obj)
        ax1 += auto_dx; ax2 += auto_dx
        ay1 += auto_dy; ay2 += auto_dy
        if ax1 <= 0 or ax2 >= canvas.winfo_width(): auto_dx = -auto_dx
        if ay1 <= 0 or ay2 >= canvas.winfo_height(): auto_dy = -auto_dy
        canvas.coords(auto_obj, ax1, ay1, ax2, ay2)
        canvas.after(30, animate_auto)

def pause_auto():
    global running
    running = False

def reset_all():
    global running
    running = False
    canvas.coords(player, 50, 50, 80, 80)
    canvas.coords(target, 200, 200, 220, 220)
    canvas.coords(auto_obj, 150, 150, 180, 180)
    update_status()

def update_status():
    px1, py1, px2, py2 = canvas.coords(player)
    status_label.config(text=f"Player X: {int(px1)}, Y: {int(py1)} | Auto: {'On' if running else 'Off'}")

root = tk.Tk()
root.title("Mini Animation")
root.geometry("500x500")

control_frame = tk.Frame(root)
control_frame.pack(fill="x")
tk.Button(control_frame, text="Start Auto", command=start_auto).pack(side="left", padx=5)
tk.Button(control_frame, text="Pause Auto", command=pause_auto).pack(side="left", padx=5)
tk.Button(control_frame, text="Reset", command=reset_all).pack(side="left", padx=5)

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

player = canvas.create_oval(50, 50, 80, 80, fill="blue")
target = canvas.create_oval(200, 200, 220, 220, fill="green")
auto_obj = canvas.create_rectangle(150, 150, 180, 180, fill="red")

status_label = tk.Label(root, text="Ready")
status_label.pack(fill="x")

auto_dx, auto_dy = 3, 3
running = False

root.bind("<Key>", move_player)
canvas.bind("<Button-1>", set_target)
canvas.focus_set()
root.mainloop()