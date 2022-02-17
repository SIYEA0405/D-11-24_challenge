import time
from turtle import Screen
from snack import Snack
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)

snack = Snack()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snack.up, "Up")
screen.onkey(snack.down, "Down")
screen.onkey(snack.left, "Left")
screen.onkey(snack.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snack.move()

    if snack.head.distance(food) < 15:
        food.refresh()
        snack.extend()
        score.up_score()

    if snack.head.xcor() > 280 or snack.head.xcor() < -280 or snack.head.ycor() > 280 or snack.head.ycor() < -280:
        score.reset()
        snack.reset()

    for segment in snack.segments[1:]:
        if snack.head.distance(segment) < 10:
            score.reset()
            snack.reset()

screen.exitonclick()
