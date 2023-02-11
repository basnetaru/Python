from list_coffee import MENU
from list_coffee import resources
from list_coffee import profit
is_on = True
profit = 0


def is_resource_sufficient(order_ingredients):
  # """Returns true when orders can be made,False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry! this is not enough {item}.")
            return False
    return True


def process_coins():
    # """Returns the total calculated from coins inserted"""
    print("please insert coins")
    total = int(input("Enter how many quarters: "))*0.25
    total += int(input("Enter how many dimes: ")) * 0.1
    total += int(input("Enter how many nickles: ")) * 0.5
    total += int(input("Enter how many pennies: ")) * 0.01
    return total


def is_transcation_successful(money_received, drink_cost):
    # """Returns true when the payement is accepted,or False if money is insufficient"""

    if money_received > drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


while is_on:
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_off = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee: {resources['coffee']} ")
        print(f"Money: ${profit} ")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(order_ingredients=drink["ingredients"]):
            payement = process_coins()
            if is_transcation_successful(payement, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
