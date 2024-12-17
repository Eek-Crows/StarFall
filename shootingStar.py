import tkinter as tk
import random

root = tk.Tk()
root.title("Shooting Star")
root.geometry("800x600")  
canvas = tk.Canvas(root, width=800, height=600, bg="black")
canvas.pack()
def create_shooting_star():
    x1 = random.randint(0, 400)
    y1 = random.randint(0, 300)
    speed_x = random.randint(5, 15)  
    speed_y = random.randint(5, 15)  
    tail_length = random.randint(10, 20) 
    star = canvas.create_oval(x1, y1, x1+5, y1+5, fill="white", outline="white")
    tail = []
    for i in range(tail_length):
        tail.append(canvas.create_oval(x1, y1, x1+1, y1+1, fill="white", outline="white"))
    def move_star():
        nonlocal x1, y1, speed_x, speed_y, star, tail
        x1 += speed_x
        y1 += speed_y
        for i in range(tail_length-1, 0, -1):
            canvas.coords(tail[i], canvas.coords(tail[i-1]))
        canvas.coords(tail[0], x1, y1, x1+1, y1+1)
        canvas.coords(star, x1, y1, x1+5, y1+5)
        if x1 > 800 or y1 > 600:
            canvas.delete(star)
            for t in tail:
                canvas.delete(t)
            create_shooting_star()
        else:
            canvas.after(50, move_star)
    move_star()
def create_new_star():
    create_shooting_star()
canvas.after(1000, create_new_star)  
root.mainloop()
