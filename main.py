from turtle import Screen,Turtle
from paddle import Paddle
screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Pong game")
paddle = Paddle()
turtle = Turtle()
screen.listen()
screen.onkey(paddle.up, "up")
screen.onkey(paddle.down, "down")
screen.tracer(0)
game_is_on = True
while game_is_on:
    paddle.create_paddle()
    screen.update()









screen.exitonclick()