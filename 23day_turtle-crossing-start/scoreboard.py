from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    level = 1

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.goto(-280, 270)
        self.color("black")
        self.write(arg=f"Level :{self.level}", align="left", font=FONT)

    def game_over(self):
        self.penup()
        self.ht()
        self.goto(0, 0)
        self.color("black")
        self.write(arg="Game over", align="center", font=FONT)

    def level_up(self):
        self.clear()
        self.penup()
        self.goto(-280, 270)
        self.color("black")
        self.level += 1
        self.write(arg=f"Level :{self.level}", align="left", font=FONT)

