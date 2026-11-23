import tkinter as tk

def draw(event):
    r = brush_size
    canvas.create_oval(
        event.x - r,
        event.y - r,
        event.x + r,
        event.y + r,
        fill="black",
        outline=""
    )
    coord_label.config(text=f"X: {event.x}, Y: {event.y}")

def clear_canvas():
    canvas.delete("all")

def update_brush(val):
    global brush_size
    brush_size = int(val)

root = tk.Tk()
root.title("Mouse Drawing Pad")
root.geometry("600x500")

brush_size = 5

top_frame = tk.Frame(root)
top_frame.pack(fill="x", pady=5)

coord_label = tk.Label(top_frame, text="X: 0, Y: 0")
coord_label.pack(side="left", padx=10)

tk.Button(top_frame, text="Clear", command=clear_canvas).pack(side="right", padx=10)

tk.Scale(top_frame, from_=1, to=20, orient="horizontal", command=update_brush).pack(side="right", padx=10)

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

canvas.bind("<B1-Motion>", draw)

root.mainloop()