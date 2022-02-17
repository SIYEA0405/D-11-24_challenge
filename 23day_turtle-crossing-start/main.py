import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

player = Player()
cars = CarManager()
score = Scoreboard()
screen.listen()
screen.onkey(player.go_up, "Up")

number = 0.1
game_is_on = True
while game_is_on:
    time.sleep(number)
    screen.update()

    cars.create_cars()
    cars.move()

    for car in cars.all_cars:
        if player.distance(car) < 25:
            score.game_over()
            game_is_on = False

    if player.position()[1] > 320:
        player.reset()
        score.level_up()
        number -= 0.02


screen.exitonclick()
