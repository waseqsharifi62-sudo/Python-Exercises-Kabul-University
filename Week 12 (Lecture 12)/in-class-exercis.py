import tkinter as tk
import random

def animate_ball():
    global x, y, dx, dy, running
    if running:
        x += dx
        y += dy
        if x - 20 <= 0 or x + 20 >= canvas.winfo_width():
            dx = -dx
        if y - 20 <= 0 or y + 20 >= canvas.winfo_height():
            dy = -dy
        canvas.coords(ball, x - 20, y - 20, x + 20, y + 20)
        root.after(20, animate_ball)

def click_ball(event):
    global x, y, dx, dy, score
    x1, y1, x2, y2 = canvas.coords(ball)
    if x1 <= event.x <= x2 and y1 <= event.y <= y2:
        score += 1
        score_label.config(text=f"Score: {score}")
        x = random.randint(50, canvas.winfo_width() - 50)
        y = random.randint(50, canvas.winfo_height() - 50)
        if score % 3 == 0:
            dx *= 1.2
            dy *= 1.2
        canvas.coords(ball, x - 20, y - 20, x + 20, y + 20)

root = tk.Tk()
root.title("Catch the Ball")
root.geometry("500x400")

score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack(pady=5)

canvas = tk.Canvas(root, bg="lightyellow")
canvas.pack(fill="both", expand=True)

x, y, dx, dy = 250, 200, 4, 4
score = 0
running = True

ball = canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="red")
canvas.bind("<Button-1>", click_ball)

animate_ball()
root.mainloop()