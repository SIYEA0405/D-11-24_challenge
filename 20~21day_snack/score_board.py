from turtle import Turtle
from food import Food
from snack import Snack


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as file_read:
            self.height_score = int(file_read.read())
        self.ht()
        self.goto(0, 260)
        self.color("white")
        self.score = 0
        self.write(arg=f"Score: {self.score} High Score {self.height_score}", align="center", font=("Arial", 20, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score {self.height_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.height_score:
            self.height_score = self.score
        with open("data.txt", mode="w") as add_score:
            add_score.write(str(self.height_score))
        self.score = 0
        self.update_scoreboard()

    def up_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game over", align="center", font=("Arial", 28, "normal"))





