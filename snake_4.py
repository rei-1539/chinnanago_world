import random
import sys
import tkinter as tk

import unko

root = tk.Tk()
root.title('Snake')
root.geometry('460x420')

height = 420
width = 460
gap = 50
x = width / 2
y = 10
wall_x = random.randint(10, width-60)
wall_y = height
a = 0
b = 0
t = True

canvas = tk.Canvas(root, width = width, height = height)
canvas.place(x=0, y=0)

def move():
    global x , y, a, b, wall_x, wall_y, t
    create_wall()
    x += a
    y += b
    if(t):
        if((x < 0 or x > width-10) or (y < 0)):
            x -= a
            y -= b
            canvas.create_rectangle(x, y, (x+10), (y+10), fill = 'Black', tag = "rectangle")
        if((x < wall_x or x > wall_x+gap-10) and (wall_y-10 < y < wall_y+10)):
            t = False
            canvas.create_text(230, 210, text = 'Game Over', font = ('', 20), tag = "word")
            canvas.create_rectangle(x-5, y-5, x+15, y+15, fill = 'Red', outline = 'Red', tag = "word")
        else:
            canvas.delete("rectangle")
            canvas.create_rectangle(x, y, (x+10), (y+10), fill = 'Black', tag = "rectangle")
        if(y > height):
            t = False
            canvas.create_text(230, 210, text = 'Clear', font = ('', 20), tag = "word")
    else:
        canvas.delete("rectangle")

    root.after(100, move)

def R(event):
    global a, b
    a=0
    a+=5
    b=0

def L(event):
    global a, b
    a=0
    a-=5
    b=0

def U(event):
    global a, b
    b=0
    b-=5
    a=0

def D(event):
    global a, b
    b=0
    b+=5
    a=0

def create_wall():
    global wall_x, wall_y
    wall_y -= 8
    canvas.delete("wall")
    canvas.create_rectangle(0 , wall_y , wall_x , wall_y+10, fill = 'gray', tag = "wall")
    canvas.create_rectangle(wall_x+gap, wall_y , width, wall_y+10, fill = 'gray', tag = "wall")
    if(wall_y < 0):
        wall_y = height
        wall_x = random.randint(10, width-60)

def Restart(event):
    global x, y, a, b, wall_x, wall_y, t
    a = b = 0
    x = width / 2
    y = 10
    wall_x = random.randint(10,width-60)
    wall_y = height
    t = True
    canvas.delete("word")

root.bind("<Right>", R)
root.bind("<Left>", L)
root.bind("<Up>", U)
root.bind("<Down>", D)

button1 = tk.Button(root, text = 'Restart', width = 10)
button1.bind("<Button-1>", Restart)
button1.place(x=0, y=0)

move()

root.mainloop()