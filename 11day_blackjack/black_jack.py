from black_jack_art import logo
import random
import os
# from replit import clear

clear = lambda: os.system('clear')


def loop():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.shuffle(cards)
    start = input("Do you want to play a game Blackjack? Type 'y' or 'n': ").lower()
    if (start == "y") or (start == "yes"):
        computer_cards = [cards.pop() for i in range(2)]
        user_cards = [cards.pop() for i in range(2)]
        # 아래는 디버깅을 위해 강제로 computer_cards가 11과 10이 나오게 해놓음
        # computer_cards = [11, 10]
        # user_cards = [11, 10]

        computer_score = sum(computer_cards)
        user_score = sum(user_cards)

        print(f"Your cards {user_cards} current score :{user_score}")
        print(f"computer's first card: {computer_cards[0]}\n")
        # 아래는 디버깅을 위한 컴퓨터의 출력문
        # print(f"computer's cards {computer_cards} current score :{computer_score}")

        number = [10, 11], [11, 10]
        computer_black_jack = "computer's black_jack. computer's winner"
        user_black_jack = "user's black_jack. user's winner"
        Type = False

        def result(A, B):
            if A > 21:
                return "user's winner"
            elif B > 21:
                return "computer's winner"
            elif A == B:
                return "Draw"
            elif A > B:
                return "computer's winner"
            elif A < B:
                return "user's winner"

        def black_jack(com_, user_):
            nonlocal Type
            for N in number:
                if N == com_:
                    Type = True
                    print(
                        f"Computer cards {computer_cards} and total score {computer_score}\nUser cards {user_cards} and total score {user_score}")
                    print(computer_black_jack)
                    return True
                elif N == user_:
                    Type = True
                    print(
                        f"Computer cards {computer_cards} and total score {computer_score}\nUser cards {user_cards} and total score {user_score}")
                    print(user_black_jack)
                    return True

        def more_cards():
            answer = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if (answer == "n") or (answer == "no"):
                return print("Good bye")
            else:
                return answer

        def user_add_deck(user_total_cards, user_total_score):
            X = cards.pop()
            new_user_total_cards = [X] + user_total_cards
            new_user_total_score = X + user_total_score
            print(f"Your cards {new_user_total_cards} current socre :{new_user_total_score}")
            return new_user_total_cards, new_user_total_score

        def computer_add_deck(computer_total_cards, computer_total_score):
            new_computer_total_cards = computer_total_cards
            new_computer_total_score = computer_total_score
            while new_computer_total_score < 16:
                Z = cards.pop()
                new_computer_total_cards = [Z] + computer_total_cards
                new_computer_total_score = Z + computer_total_score
            return new_computer_total_cards, new_computer_total_score

        def restart():
            answer = input("\nRe game? Type 'y' or 'n' ").lower()
            if (answer == "yes") or (answer == "y"):
                clear()
                loop()
            elif (answer == "no") or (answer == "n"):
                print("Good Bye")
                clear()

        game_end = black_jack(com_=computer_cards, user_=user_cards)
        if game_end:
            restart()
        elif Type == False:
            while more_cards() == "y":
                user_cards, user_score = user_add_deck(user_total_cards=user_cards, user_total_score=user_score)
                if user_score > 21:
                    print(result(A=computer_score, B=user_score))
                    print()
                    restart()

            computer_cards, computer_score = computer_add_deck(computer_total_cards=computer_cards,
                                                               computer_total_score=computer_score)
            print(result(A=computer_score, B=user_score))
            print()
            print(
                f"Computer cards {computer_cards} and total score {computer_score}\nUser cards {user_cards} and total score {user_score}")
            restart()

    else:
        print("Good Bye")


loop()
