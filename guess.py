import random
random_number = random.randint(1, 100)
game_level = input("Type 'easy' or 'hard' game to play: ").lower()


guessed = False
remaining_attempts_easy = 10
remaining_attempts_hard = 5


def easy_level(guess_number_function, random_number_function):
    global remaining_attempts_easy, guessed

    if guess_number_function == random_number_function:
        print("You entered the correct number.")
        guessed = True
    elif guess_number_function != random_number_function:
        if guess_number_function > random_number_function:

            remaining_attempts_easy -= 1
            print(
                f"You guessed the wrong number. Lower number please! You have {remaining_attempts_easy} left")

        elif random_number_function > guess_number_function:
            remaining_attempts_easy -= 1
            print(
                f"You guessed the wrong number. Higher number please! You have {remaining_attempts_easy} left")

def hard_level(guess_number_function_hard, random_number_function_hard):

    global remaining_attempts_hard, guessed
    if guess_number_function_hard== random_number_function_hard:
        print("You entered the correct number.")
        guessed = True
    elif guess_number_function_hard!= random_number_function_hard:

        if guess_number_function_hard > random_number_function_hard:

            remaining_attempts_hard -= 1
            print(
                f"You guessed the wrong number. Higher number please! You have {remaining_attempts_hard} left")

        elif random_number_function_hard > guess_number_function_hard:
            remaining_attempts_hard -= 1
            print(
                f"You guessed the wrong number. Lower number please! You have {remaining_attempts_hard} left")

while guessed == False and remaining_attempts_easy > 0:
    guess_number = int(input("Guess the number from 1 to 100: "))

    easy_level(guess_number_function=guess_number,
               random_number_function=random_number)
    hard_level(guess_number_function_hard=guess_number,
               random_number_function_hard=random_number)




while guessed == False and remaining_attempts_hard > 0:
    guess_number = int(input("Guess the number from 1 to 100: "))

    # hard_level(guess_number_function_hard=guess_number,
    #            random_number_function_hard=random_number)

if game_level == "easy":
    easy_level(guess_number_function=guess_number,
               random_number_function=random_number)
elif game_level == "hard":
    hard_level(guess_number_function_hard=guess_number,
               random_number_function_hard
               =random_number)
