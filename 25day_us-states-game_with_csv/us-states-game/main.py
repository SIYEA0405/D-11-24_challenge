'''
중단된 프로젝트 console, Terminal 실행을 시키면 오류메세지가 나온다.
2022-02-18 18:48:10.133 Python[907:9246] TSM AdjustCapsLockLEDForKeyTransitionHandling - _ISSetPhysicalKeyboardCapsLockLED Inhibit
해당 메세지는 파이썬 내부의 문제? 라는 것 같다.
'''

import turtle
import pandas
import pandas as pd
from write_states import State

screen = turtle.Screen()
screen.title("U.S. states games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

pd_data = pd.DataFrame(data, columns=["state", "x", "y"])
# for index, series in pd_data.iterrows():
#     word = series.to_dict()
#     State(word["state"], word["x"], word["y"])

data_state = data["state"].tolist()
data_x = data["x"].tolist()
data_y = data["y"].tolist()

corret_number = ""
#정답을 맞출 때 마다 아래의 맞춘숫자 부분에 더해주어야 한다
answer_states = screen.textinput(title=f"#맞춘숫자/{len(data_state)} States Correct", prompt="What another state's name?").lower()
#answer_states 가 ohio 라면 ohio 라는 turtle을 생성한다.
for index, series in pd_data.iterrows():
    word = series.to_dict()
    if answer_states in word:
        State(word["state"], word["x"], word["y"])


# screen.exitonclick()
