import random
ask=input("Type 'easy' to play easy level or 'hard' to play hard level: ").lower()
guess_number = int(input("Guess a number between 1 to 100: "))
counter_easy=10
counter_hard=5
end_of_game=False
def easy_level(guess_num,random_number_num):
    global counter_easy
    if guess_num==random_number_num:
        print("You guessed the right number!")
        end_of_game=True
    elif guess_num!=random_number_num:
        if guess_num>random_number_num:
            counter_easy-=1
            print(f"Lower number please. You have {counter_easy} attempts left")
            if counter_easy==0:
                print("You lost!")
        elif random_number_num>guess_num:
            counter_easy-=1
            print(f"Higher number please. You have {counter_easy} attempts left")
            if counter_easy==0:
                print("You lost!")
def hard_level(guess,random_number):
    global counter_hard
    if guess==random_number:
        print("You guessed the right number!")
        end_of_game=True
    elif guess!=random_number:
        if guess>random_number:
            counter_hard-=1
            print(f"Lower number please. You have {counter_hard} attempts left")
            if counter_hard==0:
                print("You lost!")
        elif random_number>guess:
            counter_hard-=1
            print(f"Higher number please. You have {counter_hard} attempts left")
            if counter_hard==0:
                print("You lost!")
if ask=="easy":
    easy_level(guess_num=guess_number, random_number_num
    =random.randint(1, 100))
# if ask=="easy":
#     easy_level(guess=guess_number, random_number=random.randint(1, 100))
elif ask=="hard":
    hard_level(guess=guess_number, random_number=random.randint(1, 100))
else:
    print("Invalid!")


while end_of_game==False and counter_hard>0 and ask=="hard":
    guess_number = int(input("Guess a number between 1 to 100: "))
    hard_level(guess=guess_number, random_number=random.randint(1, 100))
while end_of_game==False and counter_easy>0 and ask=="easy":
    guess_number = int(input("Guess a number between 1 to 100: "))
    easy_level(guess_num=guess_number, random_number_num=random.randint(1, 100))

