import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors]
choice = int(input("Type 0 for rock,1 for paper and 2 for scissors: "))
print("You chose: ")
print(list[choice])
computer_choice = random.randint(0, 2)
print("Computer chose: ")
print(list[computer_choice])

if choice >= 3:
    print("Invalid number!")
elif choice == 0 and computer_choice == 2:
    print("You won!")
elif computer_choice == 0 and choice == 2:
    print("You lost!")
elif computer_choice > choice:
    print("You lost!")
elif choice > computer_choice:
    print("You won!")
elif computer_choice == choice:
    print("Draw")
