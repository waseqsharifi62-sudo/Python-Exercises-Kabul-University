import tkinter as tk

def on_motion(event):
    coord_label.config(text=f"X: {event.x}, Y: {event.y}")

def on_left_click(event):
    click_label.config(text="Left Click")

def on_double_click(event):
    current = int(double_click_label.cget("text").split(": ")[1])
    double_click_label.config(text=f"Double Clicks: {current + 1}")

def on_enter(event):
    status_label.config(text="Mouse inside frame")

def on_leave(event):
    status_label.config(text="Mouse outside frame")

root = tk.Tk()
root.title("Mouse Event Tracker")
root.geometry("400x400")

status_label = tk.Label(root, text="Mouse outside frame")
status_label.pack(pady=5)

coord_label = tk.Label(root, text="X: 0, Y: 0")
coord_label.pack()

click_label = tk.Label(root, text="No Click")
click_label.pack()

double_click_label = tk.Label(root, text="Double Clicks: 0")
double_click_label.pack()

frame = tk.Frame(root, bg="lightgray", width=300, height=200)
frame.pack(pady=20)
frame.pack_propagate(False)

frame.bind("<Motion>", on_motion)
frame.bind("<Button-1>", on_left_click)
frame.bind("<Double-Button-1>", on_double_click)
frame.bind("<Enter>", on_enter)
frame.bind("<Leave>", on_leave)

root.mainloop()