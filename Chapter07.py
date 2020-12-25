# input()用户输入字符串
message = input("Tell me your last name please: ")
print(f"\nHello, {message.title()}!")

# 当提示内容很长时，将提示赋给一个变量
promt = "If you tell us who you are, we can personalize the messages you see."
promt += "\nWhat is your first name? "

name = input(promt)
print(f"\nHello, {name.title()}!")

# int()将input引入的字符串变为数值，可进行运算
age = input("How old are you? ")
age = int(age)
print(f"\nYou are so young!")

# Exercise 7-1
car = input("Which brand of vehicles you prefer? ")
print(f"Let me see if I can find you a {car}.")

# Exercise 7-2
num = input("How many person would come? ")
num = int(num)
if num > 8:
    print("Sorry, no avaliable table for you.")
else:
    print("Table reserved!")

# Exercise 7-3
count = input("Please insert a number: ")
count = int(count)
if count % 10 == 0:
    print(f"{count} 是10的整数倍。")
else:
    print(f"{count}不是10的整数倍。")

# 使用标志（flag）来调整状态
msg_1 = "Hi, you can tell me something about yourself. (Enter quit to end the program)"
msg_1 += "How old are you?"
active = True
while active:
    age = input(msg_1)
    if age == "quit":
        active = False
    else:
        print(age)

# 使用break终止while
msg_1 = "Please enter the name of a city you have visited:"
msg_1 += "\n(Enter quit when you are finished)"
while True:
    city = input(msg_1)
    if city == "quit":
        break
    else:
        print(f"I'd love to go to {city}")

# continue返回循环开头确认是否继续循环
cur_num = 0
while cur_num < 10:
    cur_num += 1
    if cur_num % 2 == 0:
        continue
    print(cur_num)

# Exercise 7-5

while True:
    age = input("How old are you?" )
    if age == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            print("Free ticket for you!")
        elif age < 12:
            print("The ticket price is 10 dollars.")
        else:
            print("The ticket price is 15 dollars.")

# while处理列表和字典
# 在两个列表之间用pop移除末尾值、赋值并使用append添加数值
list_1 = ['alice', 'brude', 'cicely']
list_2 = []
while list_1:
    name = list_1.pop()
    print(f"{name.title()} is in processing...")
    list_2.append(name)
print(list_2)

