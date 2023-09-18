from turtle import *
import random

color = ['red', 'green', 'blue', 'yellow', 'purple', 'black', 'orange', 'cyan',]

win = Turtle()
win.speed(0)
win.pensize(5)
title('Master Anupam\'s Drawing')

def up():
    win.setheading(90)
    win.forward(100)

def down():
    win.setheading(270)
    win.forward(100)

def right():
    win.setheading(0)
    win.forward(100)

def left():
    win.setheading(180)
    win.forward(100)

def clickLeft(x, y):
    win.color(random.choice(color))

def clickRight(x, y):
    win.stamp()

onscreenclick(clickLeft, 1)
onscreenclick(clickRight, 3)

listen()

onkey(up, 'Up')
onkey(down, 'Down')
onkey(right, 'Right')
onkey(left, 'Left')

mainloop()