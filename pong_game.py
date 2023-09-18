import turtle
import os

# Functions
def paddle_a_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)


def paddle_a_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddle_b_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddle_b_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


win = turtle.Screen()
win.title('Pong game')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

score_a = 0
score_b = 0

# paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('white')
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# paddle B
paddleB = turtle.Turtle()
paddleB.speed(-1)
paddleB.shape('square')
paddleB.color('white')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(340, 0)

# ball
ball = turtle.Turtle()
ball.speed(5)
ball.shape('circle')
ball.shapesize(1)
ball.color('red')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f'Player A: {score_a} Player B: {score_b}', align='center', font=('courier', 25, 'bold'))

# keyboard binding
win.listen()
win.onkeypress(paddle_a_up, 'w')
win.onkeypress(paddle_a_down, 's')
win.onkeypress(paddle_b_up, 'Up')
win.onkeypress(paddle_b_down, 'Down')

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system('aplay /home/anupam/python_projects/pong_bounce.wav&')
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        os.system('aplay /home/anupam/python_projects/pong_bounce.wav&')

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f'Player A: {score_a} Player B: {score_b}', align='center', font=('courier', 25, 'bold'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f'Player A: {score_a} Player B: {score_b}', align='center', font=('courier', 25, 'bold'))

    # ball and paddle collision
    if (ball.xcor() > 318 and ball.xcor() < 350) and (ball.ycor() < paddleB.ycor() + 40) and (ball.ycor() > paddleB.ycor() - 40):
        ball.setx(318)
        ball.dx *= -1
        os.system('aplay /home/anupam/python_projects/pong_bounce.wav&')
        
    if (ball.xcor() < -324 and ball.xcor() > -350) and (ball.ycor() < paddleA.ycor() + 40) and (ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-324)
        ball.dx *= -1 
        os.system('aplay /home/anupam/python_projects/pong_bounce.wav&')