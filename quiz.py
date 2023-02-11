print("welcome to quiz game developed by Aryan Basnet")
ask=input("Do you want to play, if so then type 'yes':  ").lower()
q_1=input("Which is the biggest country in the world: ").lower()
q_2=input("What is the capital city of kathmandu: ").lower()
q_3=input("What is the capital city of India").lower()
score=0
def function_1(question_1):
    global score
    if question_1=="russia":
        print("Correct answer!")
        score+=1
        print(f"Your score is {score}")

    else:
        print("Wrong answer!.You lost!")

function_1(question_1=q_1)

def function_2(question_2):
    global score
    if question_2=="kathmandu":
        print("Correct answer!")
        score+=1
        print(f"Your score is {score}")
    else:
        print("Wrong answer! You lost.")
function_2(question_2=q_2)

def function_3(question_3):
    global score
    if question_3=="new delhi":
        print("Correct answer")
        score+=1
        print(f"Your score is {score}")
    else:
        print("Wrong number")
function_3(question_3=q_3)

