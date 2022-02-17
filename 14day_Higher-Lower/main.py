from art import logo, vs
import random
from game_data import data


def clear():
    import os

    os.system("clear")


random_data_A = random.choice(data)
random_data_B = random.choice(data)
user_score = 0
continues = True

while continues:

    def format_data(random_data):
        """data에서 A의 이름, 출시한 날짜 프린트 하기 B의 이름, 출시한 날짜 프린트"""
        name = random_data["name"]
        day = random_data["release day, month"]
        return f"Name :{name}, Release day :{day}"

    # 랜덤으로 data 가지고 오기
    random_data_A = random_data_B
    random_data_B = random.choice(data)
    while random_data_A == random_data_B:
        random_data_B = random.choice(data)

    # 아스키 아트 출력
    print(logo)
    print(f"Type A: {format_data(random_data_A)}")
    print(vs)
    print(f"Type B: {format_data(random_data_B)}")

    # 두 게임중에 어떤 게임이 먼저 출시했는가(값이 더 작은쪽이 승리)
    def day_comparion(user_answer, release_A, release_B):
        """ "두 게임중에 어떤 게임이 먼저 출시했는가(값이 더 작은쪽이 승리)"""
        if release_A < release_B:
            return user_answer == "a"
        elif release_A > release_B:
            return user_answer == "b"

    # 사용자가 A나 B를 선택해서 답을 맞췄는지
    user_answer = input("Your answer Type 'A' or 'B': ").lower()
    ##각 data의 출시년도만 비교해서 A가 먼저나왔는지 B가 먼저나왔는지
    correct = day_comparion(
        user_answer,
        release_A=random_data_A["release"],
        release_B=random_data_B["release"],
    )
    clear()
    # 유저가 입력한 값이 정답이라면 "You're right. score" 를 입력하고 스코어를 더하고 게임을 계속한다
    # 유저가 입력한 값이 틀렸다면 "Wrong. score"를 입력하고 게임을 끝낸다
    if correct == True:
        user_score += 1
        print(f"You're right! You're score is :{user_score}\n")
    elif correct == False:
        continues = False
        print(f"You're lose! You're score is :{user_score}\n")

# 이 게임은 반복되어야 한다

# B에 있던 값을 A로 올린다

# 매 결과마다 새로운 화면을 출력한다
