name_1 = input("Enter your name: ")
name_2 = input("Enter their name: ")
combined_name = name_1+name_2.lower()
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
true = t+r+u+e

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")

love = l+o+v+e

love_score = love + true
# print(type(love_score))

if (love_score < 10) or (love_score > 90):
    print(
        f"You love score is {love_score},you go toether like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your love score is {love_score},You're alright together.")
else:
    print(f" Your love score is {love_score}")
