from name_higher import data
from art_higher import logo
import random
print(logo)
random_name_1 = random.choice(list)
random_name_2 = random.choice(list)
name_1 = random_name_1["name"]
name_1_follower_count = random_name_1["follower count"]
name_1_follower_description = random_name_1["description"]
name_1_follower_country = random_name_1["country"]
name_2 = random_name_2["name"]
name_2_follower_count = random_name_2["follower count"]
name_2_follower_description = random_name_2["description"]
name_2_follower_country = random_name_2["country"]
end_of_game = False


def person_1(man_1_name, man_1_follower_count, man_1_follower_description, man_1_country):
    print(
        f"Compare A: {man_1_name}, a{man_1_follower_description}, from{man_1_country}    ")


person_1(man_1_name=name_1, man_1_follower_account=name_1_follower_count,
         man_1_follower_description=name_1_follower_description, man_1_country=name_1_follower_country)


def person_2(man_2_name, man_2_follower_count, man_2_follower_description, man_2_country):
    print(
        f"Compare B: {man_2_name}, a{man_2_follower_description}, from{man_2_country}")


person_1(man_2_name=name_2, man_2_follower_account=name_2_follower_count,
         man_2_follower_description=name_2_follower_description, man_2_country=name_2_follower_country)


guess = input("Enter 'A' or 'B' : ").upper()


if name_1_follower_count > name_2_follower_count:
    if guess == "B":
        print("You lost the game.")
    elif guess == "A":
        person_1(man_1_name=name_1, man_1_follower_account=name_1_follower_count,
                 man_1_follower_description=name_1_follower_description, man_1_country=name_1_follower_country)
        print(logo)

        def person_2(man_2_name, man_2_follower_count, man_2_follower_description, man_2_country):
            print(
                f"Compare B: {man_2_name}, a{man_2_follower_description}, from{man_2_country}")
person_1(man_2_name=name_2, man_2_follower_account=name_2_follower_count,
         man_2_follower_description=name_2_follower_description, man_2_country=name_2_follower_country)
