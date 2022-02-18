import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_state = data["state"].tolist()
data_x = data["x"].tolist()
data_y = data["y"].tolist()
print(data_state)

answer_states = screen.textinput(title=f"#맞춘숫자/{len(data_state)} States Correct", prompt="What another state's name?")


# screen.exitonclick()
