from turtle import *
import random

def draw_circle(x, y, radius, color):
    penup()
    goto(x, y)
    pendown()
    fillcolor(color)
    begin_fill()
    circle(radius)
    end_fill()

def draw_rectangle(x, y, width, height, fill_color, outline_color):
    penup()
    goto(x, y)
    pendown()
    pencolor(outline_color)
    fillcolor(fill_color)
    begin_fill()
    for _ in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw_star(x, y, size, fill_color, outline_color):
    penup()
    goto(x, y)
    pendown()
    pencolor(outline_color)
    fillcolor(fill_color)
    begin_fill()
    for _ in range(5):
        forward(size)
        right(144)
    end_fill()

def draw_snow(x, y):
    draw_circle(x, y, 2, "white")

speed(0)
Screen().bgcolor("darkblue")

#Background
draw_rectangle(-250, -250, 500, 500, "darkblue", "darkblue")

#Tree Trunk
draw_rectangle(-15, -90, 30, 40, "brown", "brown")

#Start position and tree width
y = -70
width = 240
height = 25

#Green section of tree
while width > 20:
    width -= 30
    x = 0 - width / 2
    draw_rectangle(x, y, width, height, "green", "green")
    y += height

#Star
draw_star(-15, 130, 30, "yellow", "yellow")

#Snow
for _ in range(200): 
    x_snow = random.randint(-250, 250)
    y_snow = random.randint(-250, 250)
    draw_snow(x_snow, y_snow)

hideturtle()
done()

