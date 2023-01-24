from logo_calculator import logo


def add(num1, num2):
    return num1+num2


def sub(num1, num2):
    return num1+num2


def mul(num1, num2):
    return num1*num2


def div(num1, num2):
    return num1/num2


symbols = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    print(logo)
    should_continue = True
    num1 = int(input("Enter the first number: "))
    while should_continue:
        for symbols_calculator in symbols:
            print(symbols_calculator)
        calculation = input("Enter the sign that you want to enter: ")
        num2 = int(input("Enter the another number: "))
        calculation_function = symbols[calculation]
        answer = calculation_function(num1, num2)
        print(f"  {num1}  {calculation} {num2} = {answer}")

        continue_loop = input(
            "Type 'yes' to continue and 'new' to restart the calculator:  ")
        if continue_loop == "yes":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
