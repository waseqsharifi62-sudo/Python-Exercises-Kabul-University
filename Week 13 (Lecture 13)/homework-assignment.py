import tkinter as tk
import random

class MiniGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Game")
        self.root.geometry("600x500")

        self.running = False
        self.score = 0

        self.top_frame = tk.Frame(root)
        self.top_frame.pack(fill="x")

        self.score_label = tk.Label(self.top_frame, text="Score: 0")
        self.score_label.pack(side="left", padx=10)

        self.start_btn = tk.Button(self.top_frame, text="Start", command=self.start)
        self.start_btn.pack(side="left", padx=5)

        self.pause_btn = tk.Button(self.top_frame, text="Pause", command=self.pause)
        self.pause_btn.pack(side="left", padx=5)

        self.reset_btn = tk.Button(self.top_frame, text="Reset", command=self.reset)
        self.reset_btn.pack(side="left", padx=5)

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill="both", expand=True)

        self.player = self.canvas.create_rectangle(50, 50, 90, 90, fill="blue", tags="player")
        self.enemy = self.canvas.create_oval(200, 200, 240, 240, fill="red", tags="enemy")
        self.coin = self.canvas.create_oval(300, 300, 320, 320, fill="gold", tags="coin")

        self.edx, self.edy = 4, 4

        self.root.bind("<Key>", self.move_player)
        self.canvas.bind("<Button-1>", self.shoot)
        self.canvas.focus_set()

    def start(self):
        self.running = True
        self.animate()

    def pause(self):
        self.running = False

    def reset(self):
        self.running = False
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.canvas.coords(self.player, 50, 50, 90, 90)
        self.canvas.coords(self.enemy, 200, 200, 240, 240)
        self.canvas.coords(self.coin, 300, 300, 320, 320)
        self.edx, self.edy = 4, 4

    def move_player(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        speed = 10
        nx1, ny1, nx2, ny2 = x1, y1, x2, y2

        if event.keysym == "Up": ny1 -= speed; ny2 -= speed
        elif event.keysym == "Down": ny1 += speed; ny2 += speed
        elif event.keysym == "Left": nx1 -= speed; nx2 -= speed
        elif event.keysym == "Right": nx1 += speed; nx2 += speed
        elif event.keysym == "w": ny1 -= speed; ny2 -= speed
        elif event.keysym == "s": ny1 += speed; ny2 += speed
        elif event.keysym == "a": nx1 -= speed; nx2 -= speed
        elif event.keysym == "d": nx1 += speed; nx2 += speed

        if nx1 >= 0 and nx2 <= self.canvas.winfo_width() and ny1 >= 0 and ny2 <= self.canvas.winfo_height():
            self.canvas.coords(self.player, nx1, ny1, nx2, ny2)

    def shoot(self, event):
        items = self.canvas.find_overlapping(event.x-5, event.y-5, event.x+5, event.y+5)
        if self.coin in items:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.coords(self.coin, random.randint(50, 500), random.randint(50, 400), random.randint(50, 500), random.randint(50, 400))
            cx1, cy1, cx2, cy2 = self.canvas.coords(self.coin)
            self.canvas.coords(self.coin, cx1, cy1, cx1+20, cy1+20)

    def animate(self):
        if self.running:
            ex1, ey1, ex2, ey2 = self.canvas.coords(self.enemy)
            ex1 += self.edx; ex2 += self.edx
            ey1 += self.edy; ey2 += self.edy

            if ex1 <= 0 or ex2 >= self.canvas.winfo_width(): self.edx = -self.edx
            if ey1 <= 0 or ey2 >= self.canvas.winfo_height(): self.edy = -self.edy

            self.canvas.coords(self.enemy, ex1, ey1, ex2, ey2)
            self.root.after(20, self.animate)

root = tk.Tk()
app = MiniGame(root)
root.mainloop()