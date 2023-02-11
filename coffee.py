
from list_coffee import MENU

print("Welcome to the digital coffee machaine")
choice=input("What would you like, (espresso/latte/cappuccino): ").lower()
water=300
milk=200
coffee=100
money=0
remaining_amount=0
#prices
total_espresso=1.50
total_latte=2.50
total_cappuccino=3.00
total_price=0
def report():
    print(f"Water: {water}ml")
    print(f"Milk : {milk}ml ")
    print(f"Coffee: {coffee}g ")
    print(f"Money: ${money} ")

#money

coins=print("Please insert coins")
quarters=float(input("How many quarters? "))
dimes=float(input("How many dimes? "))
nickles=float(input("How many nickles? "))
pennies=float(input("How many pennies? "))
end_of_game=False

# function to print the report



if choice == "report":
    report()
def espresso(odor,quarters_price,dimes_price,nickles_price,pennies_price):
    global money,remaining_amount,total_price,coffee,milk,water

    if odor=="espresso":
        total_price= float ((quarters_price*0.25)+(dimes_price*0.10)+(nickles_price*0.05)+(pennies_price*0.01))
        if total_price>MENU["espresso"]["cost"]:
            remaining_amount= round(total_price-MENU["espresso"]["cost"],2)
            water -= 50
            coffee -= 18
            print(f"Here is  {remaining_amount} in change. ")
        elif MENU["espresso"]["cost"]<total_price:
            print("More money is required")
        elif MENU["espresso"]["cost"]==total_price:
            water -= 50
            coffee -= 18
            print(f"Here is {remaining_amount} in change")
        elif water<=50 and coffee<=18:
            end_of_game=True
            print("Coffee is finished!")



espresso(odor=choice,quarters_price=quarters,dimes_price=dimes,nickles_price=nickles,pennies_price=pennies)


def latte(odor_1 , quarters_price_1,dimes_price_1,nickles_price_1,pennies_price_1):
    global money, remaining_amount,total_price,water,coffee,milk

    if odor_1 == "latte":
        total_price = float(
            (quarters_price_1 * 0.25) + (dimes_price_1 * 0.10) + (nickles_price_1 * 0.05) + (pennies_price_1 * 0.01))
        if total_price > MENU["latte"]["cost"]:
            water -= 50
            coffee -= 18
            remaining_amount = round(total_price - MENU["latte"]["cost"], 2)
            print(f"Here is  {remaining_amount} in change. ")
        elif MENU["latte"]["cost"] < total_price:
            print("More money is required")
        elif MENU["latte"]["cost"] == total_price:
            print(f"Here is {remaining_amount} in change")
        elif milk<=150 and coffee<=24 and water<=200:
            end_of_game=True
            print("Coffee is finished!")


latte(odor_1=choice, quarters_price_1=quarters, dimes_price_1=dimes, nickles_price_1=nickles, pennies_price_1=pennies)


def cappuccino(odor_2,quarters_price_2,dimes_price_2,nickles_price_2,pennies_price_2):
    global money,remaining_amount,total_price,water,milk,coffee

    if odor_2 == "cappuccino":
        total_price = float(
            (quarters_price_2 * 0.25) + (dimes_price_2 * 0.10) + (nickles_price_2 * 0.05) + (pennies_price_2 * 0.01))
        if total_price > MENU["cappuccino"]["cost"]:
            remaining_amount = round(total_price - MENU["cappuccino"]["cost"], 2)
            water -= 50
            coffee -= 18
            print(f"Here is  {remaining_amount} in change. ")
        elif MENU["cappuccino"]["cost"] < total_price:
            print("More money is required")
        elif MENU["cappuccino"]["cost"] == total_price:
            print(f"Here is {remaining_amount} in change")
        elif milk <= 100 and coffee <= 24 and water <= 250:
            end_of_game=True


cappuccino(odor_2=choice, quarters_price_2=quarters, dimes_price_2=dimes, nickles_price_2=nickles, pennies_price_2=pennies)

while end_of_game!=True and choice == "espresso" and water>=50 and coffee>=18 :
    choice = input("What would you like, (espresso/latte/cappuccino): ").lower()
    espresso(odor=choice, quarters_price=quarters, dimes_price=dimes, nickles_price=nickles, pennies_price=pennies)

while end_of_game:
    choice = input("What would you like, (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        end_of_game=True
    elif choice=="report"
        report()












