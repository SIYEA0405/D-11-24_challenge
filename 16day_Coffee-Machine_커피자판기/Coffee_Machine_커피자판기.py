from coffee_data import MENU, resources

sales = 0
machine_answer = True


# 커피 머신 프로그램 요구 사항
# Todo: 1. 사용자에게 "무엇을 원하십니까?"라고 묻습니다. (에스프레소, 라테, 카푸치노)

def coffee_recipe(order):
    """각 커피 메뉴들의 레시피"""
    return MENU[order]["ingredients"]


def coffee_cost(order):
    """각 커피 메뉴들의 가격"""
    return MENU[order]["cost"]


def machine_report():
    print(resources)
    print(round(sales, 2))


def machine_stock(order_recipe):
    for resource in resources:
        if resource in order_recipe:
            if resources[resource] >= order_recipe[resource]:
                # water :300
                # milk :200
                # coffee :100
                resource_stock = resources[resource]
                # coffee_recipe(order)
                # water: 50
                # coffee: 18
                resource_usage = order_recipe[resource]
                # water :250
                # milk :200
                # coffee :82
                remaining_stock = resource_stock - resource_usage
                resources[resource] = remaining_stock
            elif resources[resource] < order_recipe[resource]:
                return False
    return True


def add_cost():
    cent_25 = float(input("How many 25 cents? : ")) * (0.25)
    cent_10 = float(input("How many 10 cents? : ")) * (0.10)
    cent_5 = float(input("How many 5 cents? : ")) * (0.05)
    cent_1 = float(input("How many 1 cents? : ")) * (0.01)
    return cent_25 + cent_10 + cent_5 + cent_1


while True:
    order = input("What do you want Type: 'espresso', 'latte', 'cappuccino'\n: ").lower()
    if order == "off":
        break
    elif order == "report":
        machine_report()
    elif order in ('espresso', 'latte', 'cappuccino'):
        order_recipe = coffee_recipe(order)
        sales += coffee_cost(order)
        machine_answer = machine_stock(order_recipe)
        if not machine_answer:
            print("Sorry there is not enough water.")
        change = add_cost() - coffee_cost(order)
        if change > 0:
            print(f"Here is {round(change, 2)} dollars in change.")
            print(f"Here is your {order}. Enjoy!")
        elif change < 0:
            print("Sorry that's not enough money. Money refunded.")
            sales -= coffee_cost(order)

    # a. 사용자의 입력을 확인하여 다음에 수행할 작업을 결정합니다.
# b. 프롬프트는 동작이 완료될 때마다 표시되어야 한다. 예를 들어 음료가 나간 뒤에 다음 고객을 응대하기 위해 프롬프트가 다시 표시되어야 합니다.
# Todo: 2. 프롬프트에 "off"를 입력하여 커피 머신을 끕니다.
# Todo: 3. 보고서를 인쇄합니다.

# a. 커피머신 관리자는 커피머신 전원을 끄는 비밀 단어로 "off"를 사용할 수 있다. 경우 코드가 실행을 종료해야 합니다.
# a. 사용자가 프롬프트에 "report"를 입력할 때, 다음을 나타내는 보고서가 생성되어야 한다.
# 예) 현재 재고 물량:
# 물: 100ml
# 우유: 50ml
# 커피: 76g
# 매출: $2.5
# Todo: 4. 재고가 충분한지 확인하기
# a. 사용자가 음료수를 선택할 때 프로그램은 음료를 만들수 있을만큼 재고가 충분한지 확인해야 합니다.
# b. 예를 들어, 라떼에 200ml의 물이 필요한데 기계에 100ml밖에 남지 않았을 경우,
# 음료를 만들지 말고 "Sorry there is not enough water."라고 인쇄해야 합니다.
# c. 우유나 커피와 같은 다른 재고가 부족할 경우에도 동일한 현상이 발생하여야 한다.
# Todo: 5. 동전으로 결제하기
# a. 음료를 제조하기에 충분한 재고가 있다면, 프로그램은 사용자에게 동전을 넣으라는 메시지를 표시합니다.
# b. 25센트 = 0.25, 10센트 = 0.10달러, 5센트 = 0.05, 1센트 = 0.01달러라는 점을 기억하십시오.
# c. 삽입된 동전의 화폐 가치를 계산합니다. 예: 25센트 1개, 10센트 2개, 5센트 1개, 1센트 2개 = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# Todo: 6. 트랜잭션(거래)이 성공했는지 확인하십시오.
# a. 사용자가 선택한 음료를 구매하기에 충분한 돈을 넣었는지 확인합니다.
# 예를 들어, 라떼는 2.50달러였지만, 사용자가 0.52달러만 넣었다면 동전을 세고 난 후 프로그램에서는 "Sorry that's not enough money. Money refunded.” 을 출력해야 합니다.
# b. 사용자가 충분한 돈을 넣었다면, 음료의 비용은 매출에 더해진다. 이는 "report" 를 호출했을 때 반영되어야 합니다.
# 예)
# 물: 100ml
# 우유: 50ml
# 커피: 76g
# 매출: $2.5
# c. 사용자가 돈을 너무 많이 넣었을 경우, 기계는 잔돈을 제공해야 합니다.
# 예: "Here is $2.45 dollars in change.”"
# 잔돈은 소수점 세번째 자리에서 반올림해야 합니다.
# Todo: 7. 커피 제조하기
# 만약 거래가 성공적이고 음료를 만들기 위한 충분한 재고가 있다면 음료를 제조하는 데 사용한 재료는 재고에서 차감되어야 합니다.
# 커피 기계 재고
# 예: 라떼 구매 전 report:
# 물: 300ml
# 우유: 200ml
# 커피: 100g
# 돈: $0
# 라떼 구매 후 report:
# 물: 100ml
# 우유: 50ml
# 커피: 76g
# 돈: $2.5
# b. 모든 재고를 차감한 후에 사용자가 latte를 주문했다면 "Here is your latte. Enjoy!”. 를 출력합니다.
