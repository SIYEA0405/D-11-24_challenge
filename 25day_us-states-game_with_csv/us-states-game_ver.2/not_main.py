'''
중단된 프로젝트 console, Terminal 실행을 시키면 오류메세지가 나온다.
2022-02-18 18:48:10.133 Python[907:9246] TSM AdjustCapsLockLEDForKeyTransitionHandling - _ISSetPhysicalKeyboardCapsLockLED Inhibit
해당 메세지는 파이썬 내부의 문제? 라는 것 같다.
----해결----
=> stackoverflow: Preferences -> Keyboard -> Input Sources. There, unselect the "use the Caps Lock key..."
=> 키보드 > 입력소스 > 한/영 키로 ABC 입력 소스 전환 부분의 체크란을 해제 하니 오류가 사라졌다.(그럼 나는 한글 어떻게 써..?)
'''
import turtle
import pandas
from write_states import State

screen = turtle.Screen()
screen.title("U.S. states games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("../us-states-game_ver.1/50_states.csv")
pd_data = pandas.DataFrame(data, columns=["state", "x", "y"])
data_state = data["state"].tolist()

correct_number = 0
leftover_list = data_state

while correct_number < 50:
    answer_states = screen.textinput(title=f"{correct_number}/{len(data_state)} States Correct",
                                     prompt="What another state's name?").title()
    if answer_states == "Exit":
        break
    for index, series in pd_data.iterrows():
        word = series.to_list()
        print(word)
        if answer_states in word:
            State(word[0], word[1], word[2])
            leftover_list.remove(word[0])
            correct_number += 1
pandas.DataFrame(leftover_list).to_csv("not_main_left_list.cvs")

screen.exitonclick()
