from turtle import Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)
l_paddle = Paddle((-470, 0))
r_paddle = Paddle((470, 0))
ball = Ball()
screen.listen()
score = Scoreboard()
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()
    time.sleep(ball.move_speed)
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 450 or ball.distance(l_paddle) < 50 and ball.xcor() < -450:
        ball.bounce_back()

    if ball.xcor() > 500:
        ball.reset()
        score.l_point()

    if ball.xcor() < -500:
        ball.reset()
        score.r_point()

screen.exitonclick()
