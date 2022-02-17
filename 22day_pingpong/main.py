import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pingpong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

number = 0.1
game_is_on = True
while game_is_on:
    time.sleep(number)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320\
            or ball.distance(left_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()
        number -= 0.01

    if ball.xcor() > 400:
        ball.reset()
        ball.bounce_x()
        score_board.r_up_score()
        number = 0.1

    if ball.xcor() < -400:
        ball.reset()
        ball.bounce_x()
        score_board.l_up_score()
        number = 0.1


screen.exitonclick()
