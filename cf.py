
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
print( type(MENU["espresso"]["cost"]))

on_game=True

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]

while on_game:
    choice=input("What would you like (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        on_game=False
    elif choice=="report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee:{resources['coffee']}")
        print(f"Money: {resources['money']}")
    else:
        drink=MENU[choice]
