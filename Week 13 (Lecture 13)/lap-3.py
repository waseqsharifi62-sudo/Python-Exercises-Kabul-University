import tkinter as tk

def animate():
    global x, y, dx, dy, running
    if running:
        x += dx
        y += dy
        if x - 15 <= 0 or x + 15 >= canvas.winfo_width():
            dx = -dx
        if y - 15 <= 0 or y + 15 >= canvas.winfo_height():
            dy = -dy
        canvas.coords(ball, x - 15, y - 15, x + 15, y + 15)
        root.after(20, animate)

def start():
    global running
    if not running:
        running = True
        animate()

def pause():
    global running
    running = False

def reset():
    global x, y, dx, dy, running
    running = False
    x, y, dx, dy = 100, 100, 5, 5
    canvas.coords(ball, x - 15, y - 15, x + 15, y + 15)

def faster():
    global dx, dy
    dx *= 1.2
    dy *= 1.2

def slower():
    global dx, dy
    dx *= 0.8
    dy *= 0.8

root = tk.Tk()
root.title("Bouncing Ball")
root.geometry("400x400")

controls = tk.Frame(root)
controls.pack(fill="x")
tk.Button(controls, text="Start", command=start).pack(side="left")
tk.Button(controls, text="Pause", command=pause).pack(side="left")
tk.Button(controls, text="Reset", command=reset).pack(side="left")
tk.Button(controls, text="Faster", command=faster).pack(side="left")
tk.Button(controls, text="Slower", command=slower).pack(side="left")

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

x, y, dx, dy = 100, 100, 5, 5
running = False
ball = canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="red")

root.mainloop()