import time
from random import *

possible_food = ["apple", "orange", "crisps", "water", "juice", "chocolate",
                 "lemon", "tomato_ketchup", "milk", "blueberry", "blackberry",
                 "sauce", "chocolate_milk", "bolognese", "fish", "boiled_egg",
                 "egg_shell", "poached_egg", "fried_egg"]

items = ""

print("Hello and welcome to my game")
time.sleep(1)
print("The rules are simple, I ask you for food, you say the name of it.")
time.sleep(2)
print("If you do it correctly, you gain 1 point")
time.sleep(1)
print("If you do not do it correctly, you lose 1 point")
time.sleep(1)
score = 0
while True:
    food_index = randint(0, 18)
    food_choice = possible_food[food_index]
    answer = input(f"Feed me {food_choice}\n")

    if answer == food_choice:
        print("Yummy, you fed me correctly :)")
        score += 1
        print(f"Your score is {score}")
    else:
        print("You didn't feed me correctly :(")
        score -= 1
        print(f"Your score is {score}")
    if score <= -10:
        print("You have failed, please leave")
        time.sleep(3)
        quit()
    elif answer == "secret":
        answer_code = input("Enter the secret code for a lot of score!\n")
        if answer_code == "python":
            score = 9223372036854775806
            print("You get 9 quintillion score!")
        else:
            print("That code was wrong")
    elif answer == "hacker":
        print("no hacking 4 u")
