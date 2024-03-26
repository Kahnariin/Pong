# Simple Pong in Python 3.

import turtle
import paddle
import ball
import time


# Screen settings:

window = turtle.Screen()
window.title('Pong by @Kahnariin')  
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Components:

r_paddle = paddle.Paddle((350, 0))
l_paddle = paddle.Paddle((-350, 0))
pong_ball = ball.Ball(0, 0)

# Score variables:

r_score = 0
l_score = 0

# Keyboard bindings:

window.listen()
window.onkeypress(r_paddle.go_up, "Up")
window.onkeypress(r_paddle.go_down, "Down")
window.onkeypress(l_paddle.go_up, "w")
window.onkeypress(l_paddle.go_down, "s")


# Main game loop:

while True:
    time.sleep(.01)
    window.update()
    pong_ball.move()

    # Collision for right paddle.
    if (pong_ball.xcor() > 340 and pong_ball.xcor() < 350) and (pong_ball.ycor() < r_paddle.ycor() + 40 and pong_ball.ycor() > r_paddle.ycor() - 40):
        pong_ball.setx(340)
        pong_ball.dx *= -1
    
    # Collision for left paddle.
    if (pong_ball.xcor() < -340 and pong_ball.xcor() > -350) and (pong_ball.ycor() < l_paddle.ycor() + 40 and pong_ball.ycor() > l_paddle.ycor() - 40):
        pong_ball.setx(-340)
        pong_ball.dx *= -1

    if pong_ball.xcor() > 390:
        r_score += 1
    
    if pong_ball.xcor() < -390:
        l_score += 1