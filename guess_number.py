import random

random_number = random.randint(1, 20)
print(random)
number = int(input("Enter the number from 1 to 20: "))
while not random_number == number:
    number = input("Enter the number from 1 to 20: ")
if random_number == number:
    print("You guessed the correct number!")
elif random_number > number:
    print("Higher number please!")
elif number > random_number:
    print("Lower number please!")
