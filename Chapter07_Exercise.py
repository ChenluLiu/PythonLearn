# Exercise 7-8
sandwich_orders = ['beef', 'chicken', 'vegetable', 'ham',]
finished_sandwich = []

while sandwich_orders:
    done = sandwich_orders.pop()
    print(f"I'm making {done} sandwich now.")
    finished_sandwich.append(done)

print("\nI have made those sandwiches:")

for i in finished_sandwich:
    print(i)

# Exercise 7-9
sandwich_orders = ['beef', 'chicken', 'vegetable', 'ham', 'ham', 'ham']
print("Sorry, ham sandwich sold out!")
while 'ham' in sandwich_orders:
    sandwich_orders.remove("ham")
print("These sandwiches are avaliable:")
for i in sandwich_orders:
    print(i)

# Exercise 7-10

vacation = {}

while True:
    name = input("\nWhat is your name? ")
    place = input("\nWhere is your favorite destination for a vacation? ")
    #vacation的键是name，值是place
    vacation[name] = place
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == "no":
        break

for name, place in vacation.items():
    print(f"Hi {name.title()}, your favorite vacation place is {place}!")