MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
Money = 0
end_of_order = False


while end_of_order:
    choice = input("What do you like to take(espresso/latte/cappuccino) :")
    if choice == "report":
        print(f"Water: {resources['water']}g")
        print(f"Milk: {resources['milk']}g")
        print(f"Coffee: {resources['coffee']}g")
    elif choice == "espresso":
        if MENU[choice]["ingredients"]["water"] >= 50 and MENU[choice]["ingredients"]["coffee"] >= 18:
            Money += 100
            print(f"Money is {Money}")
        else:
            print("Money not enough.")
