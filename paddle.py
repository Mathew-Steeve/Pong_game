from turtle import Turtle
POSITION = ((470, 0), (470, 20), (470, 40))
UP = 90
DOWN = 270
MOVE_DIS = 20


class Paddle:
    def __init__(self):
        self.segment = []
        self.create_paddle()
        # self.head = self.segment[0]
        # self.tail = self.segment[2]

    def create_paddle(self):

        for pad in POSITION:
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(pad)
            self.segment.append(turtle)

    # def move(self):
    #     k = self.segment
    #     for i in range(len(k) - 1, 0, -1):
    #         new_x = k[i - 1].xcor()
    #         new_y = k[i - 1].ycor()
    #         k[i].goto(new_x, new_y)
    #     self.head.forward(MOVE_DIS)
    #
    # def up(self):
    #     if self.tail.heading() != 90 or self.head.heading() != 90:
    #         self.head.setheading(UP)
    #
    # def down(self):
    #     if self.tail.heading() != 180 or self.head.heading() != 180:
    #         self.head.setheading(DOWN)


