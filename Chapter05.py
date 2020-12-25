
# if elif else
age = 35
if age < 18:
    price = 15
elif age < 60:
    price = 25
else:
    price = 20
print(f"Your price costs {price} dollars.")

# exercise 5-3
alien_color = ["green", "yellow", "red"]
color = "green"
# color = "red"
if color == "green":
    print("You got 5 scores!")
else:
    print("You missed!")

alien_color = ["green", "yellow", "red"]
# color = "green"
color = "red"
if color == "green":
    print("You got 5 scores!")
else:
    print("You missed!")

alien_color = ["green", "yellow", "red"]
# color = "green"
# color = "red"
color = "yellow"
if color == "green":
    print("You got 5 scores!")
elif color == "red":
    print("You missed!")
else:
    print("You got 10 scores!")

# Exercise 5-6
age = 26
if age < 2:
    print("You are a baby!")
elif age >= 2 and age < 4:
    print("You are youth!")
elif age >= 4 and age <13:
    print("You are junior!")
elif age >= 13 and age <20:
    print("You are senior!")
elif age >= 20 and age < 65:
    print("You are adult!")
else:
    print("You are old!")

# Exercise 5-7
favorite_fruits = ["mango", "orange", "banana"]
if "banana" in favorite_fruits:
    print("You really like banana!")

# for and if
toppings = ["mushroom", "cheese", "green pepper"]

for topping in toppings:
    if topping == "mushroom":
        print("SORRY, we are out of mushrooms right now.")
    else:
        print(f"Add {topping}.")

print("Finish your pizza.")

# Exercise 5-8
user_list = ["admin", "lucy", "jack", "maria", "ice"]
for user in user_list:
    if user == "admin":
        print("Hello Admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, welcome!")

# Exercise 5-9
user_null = []
if user_null:
    for user in user_null:
        print(f"Hello {user.title()}!")
else:
    print("We need to find some users!")

# Exercese 5-10
current_users = ["Ai", "bi", "ci", "di", "Ei"]
new_users = ["Di", "ei", "fi", "gi", "hi"]

#for new_user in new_users:
#    if new_user in current_users:
#        print(f"User name {new_user}oppupied, use another user name please!")
#    else:
#        print(f"User name {new_user} avaliable!")

current_users = ["Ai", "bi", "ci", "di", "Ei"]
new_users = ["Di", "ei", "fi", "gi", "hi"]
current_users_lower = []

for user in current_users:
        current_users_lower.append(user.lower())

print(current_users_lower)

for user in new_users:
    if  user.lower() in current_users_lower:
        print(f"User name {user} inavaliable!")
    else:
        print(f"User name {user} avaliable!")

# Exercise 5-11
num_list = [1,2,3,4,5,6,7,8,9]

for num in num_list:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")

