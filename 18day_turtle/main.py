import turtle as t  # import Turtle, Screen
import random

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.pensize(1)
# tim.speed(5)  #test
tim.speed(0)  # real

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

hirst_color = [(208, 160, 101), (150, 75, 37), (231, 213, 97), (132, 34, 21), (191, 156, 15), (87, 33, 21),
               (238, 174, 153), (21, 57, 80), (41, 117, 63), (31, 93, 135), (196, 98, 88), (2, 81, 115), (10, 99, 77),
             (194, 163, 165), (109, 159, 185), (73, 76, 40), (179, 209, 168), (106, 140, 129), (37, 27, 35),
             (78, 153, 168), (46, 50, 47), (134, 163, 150), (234, 178, 180), (2, 72, 136), (125, 64, 66), (118, 36, 39)]

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)
# for _ in range(10):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# shape = 3
# while True:
#     for 각도 in range(shape):
#         tim.forward(50)
#         tim.right(360 / shape)
#     shape += 1
# move = [90, 180, 270, 360]

# def tim_move():
#     tim.right(random.choice(move))
#     #동 서 남 북 중 하나
#     tim.pencolor((random_color()))
#     tim.forward(20)
# def tim_move():
#     tim.pencolor(random.choice(hirst_color))
#     tim.circle(100)
#     tim.circle(5, 10)

def tim_move():
    for move in range(10):
        tim.dot(40, random.choice(hirst_color))
        tim.forward(70)
        tim.pendown()
        tim.penup()

val = -300

for go_tim in range(10):
    tim.penup()
    if val <= 300:
        tim.goto(-320, val)
        val += 80
        tim_move()


screen = t.Screen()
screen.exitonclick()
