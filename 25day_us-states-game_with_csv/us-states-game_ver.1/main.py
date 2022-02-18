import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states games")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
leftover_list = all_states
correct_number = 0

while correct_number < 50:
    answer_state = screen.textinput(title=f"{correct_number}/{len(all_states)} States Correct",
                                    prompt="What another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        leftover_list.remove(answer_state)
        correct_number += 1

pandas.DataFrame(leftover_list).to_csv("left_list.cvs")

screen.exitonclick()
