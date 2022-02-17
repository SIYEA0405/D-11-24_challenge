from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_x = 300
            new_y = random.randint(-250, 250)
            new_car.goto(new_x, new_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

