import turtle
import random
win = turtle.Turtle()
win.color('red')
win.speed(59)
win.pensize(5)
win.shape('turtle')


# while True:
#     win.left(70)
#     win.forward(100)
#     win.right(140)
#     win.forward(100)


# # This for loop creates a star
# for _ in range(5):
#     win.left(70)
#     win.forward(100)
#     win.right(140)
#     win.forward(100)


# # This creates circle
# win.penup()
# win.right(10)
# win.backward(80)
# win.pendown()

color = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'cyan']

# win.color('red', 'blue')

# win.width(5)

# win.begin_fill()  
# win.circle(100)
# win.end_fill()


# # This creates square
# win.penup()
# win.backward(150)
# win.pendown()

# win.color('yellow', 'black')
# win.width(10)
# win.begin_fill()
# for _ in range(4):
#     win.forward(100)
#     win.right(90)
# win.end_fill()


# This program randomly generate circle with random colors

for _ in range(5):
    randColor = random.randrange(0, len(color))
    win.color(color[randColor], color[random.randrange(0, len(color))])

    rand1 = random.randrange(-200, 200)
    rand2 = random.randrange(-200, 200)

    win.penup()
    win.setpos((rand1, rand2))
    win.pendown()


    win.begin_fill()
    win.circle(random.randrange(0, 80))
    win.end_fill()




turtle.mainloop()