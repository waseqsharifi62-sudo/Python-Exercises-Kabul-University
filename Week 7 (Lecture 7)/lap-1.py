import tkinter as tk

root = tk.Tk()
root.title('Advanced Programming Lab')
root.geometry('400x300')
root.minsize(300, 200)

tk.Label(root, text='Advanced Programming Lab', font=('Arial', 14, 'bold')).pack(pady=20)
tk.Button(root, text='Button 1').pack(pady=5)
tk.Button(root, text='Button 2').pack(pady=5)
tk.Button(root, text='Button 3').pack(pady=5)

region = tk.Frame(root, bg='lightblue', height=50)
region.pack(fill='x', pady=20)

root.mainloop()