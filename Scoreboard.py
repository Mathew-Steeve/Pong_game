from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier", 80, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.score_l = 0
        self.score_r = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.score_l}", False, ALIGNMENT, FONT)
        self.goto(100, 200)
        self.write(f"{self.score_r}", False, ALIGNMENT, FONT)

    def l_point(self):
        self.score_l += 1
        self.update_score()

    def r_point(self):
        self.score_r += 1
        self.update_score()
