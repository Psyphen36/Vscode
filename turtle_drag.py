import turtle
from turtle import Turtle, Screen

screen = Screen()

t = Turtle('turtle')

screen.bgcolor('black')
t.color('white')
t.speed(-1)
def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)

def clickRight(x, y):
    t.clear()

def main():
    turtle.listen()

    t.ondrag(dragging)

    turtle.onscreenclick(clickRight, 3)

    screen.mainloop()

if __name__ == '__main__':
    main()