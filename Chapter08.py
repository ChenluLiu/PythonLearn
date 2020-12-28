# 函数
def greet_user():
    print("Hello!")

greet_user()

def greet_user(user_name):
    print(f"Hello,{user_name.title()}!")

greet_user("LUCY")

# user_name为形参parameter，值“LUCY”是实参argument

def favorite_book(title):
    print(f"One of my favorite book is {title.title()}!")

favorite_book("Frog")

def make_shirt(size, note):
    print(f"The size is {size}, and the shirt prints '{note}'.")
make_shirt("m", "I love Beijing")

# 可为形参设置默认值，默认值也可以在调用时通过赋予实参进行修改
def make_shirt(size, note='I love Beijing'):
    print(f"The size is {size}, and the shirt prints '{note}'.")
make_shirt("m")
make_shirt("m", "I love Shanghai")

# 使用retrun返回值和字典
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name }
    return person

musician = build_person( 'Chenlu', 'Liu')
print(musician)

# Exersice 8-6
def city_country(city, country):
    print(f"'{city}, {country}'")
city_country('NYC', 'USA')
city_country('Beijing', 'China')
city_country('Tokyo', 'Japan')

# Exercise 8-7
def make_album(name, album = ''):
     singer = {'name': name, 'album': album}
     if album:
        singer['album'] = album
     return singer
person = make_album('Jay', '7℃')
print(person)
person = make_album('Lucy')
print(person)
person = make_album('Jolin', 'Say love')
print(person)

# Exercise 8-8
def make_doc(name, album):
    doc = {'name': name, 'album': album}
    return doc

print("enter 'q' to quit.")
while True:
    name_input = input('Please enter the name:',)
    if name_input == 'q':
        break
    album_input = input('Please enter the album: ',)
    if album_input == 'q':
        break
    singer = make_doc(name_input, album_input)
    print(singer)

# Exercise 8-9
# Exercise 8-10

def send_msgs(msgs, sent_msgs):
    while msgs:
        current_msg = msgs.pop()
        print(f"sending {current_msg}...")
        sent_msgs.append(current_msg)

messages = [
    'A',
    'B',
    'C',
    'D',
    ]
sent_messages = []
send_msgs(messages, sent_messages)
print(messages)
print(sent_messages)

# *所有值都进入*后名称的空元祖
# def A(par_1, par_2, *par_3)   前两个实参匹配par_1和par_2，后续均匹配至par_3。任意数量的形参必须放在最后
def make_pizza(size, *toppings):
    print(f"make a {size} inches pizza, with the following toppings:")
    for topping in toppings:
        print(f' - {topping}')

make_pizza(6, 'cheese', 'mushrooms')

# **任意数量的关键字实参
# Exercise 8-14
def build_cars(maker, model, **car_info):
    car_info['maker'] = maker
    car_info['model'] = model
    return car_info

car_port = build_cars('Toyota', 'S100', color = 'black', tow_package = True)
print(car_port)

# import A 代表导入A.py的全部模块
# 调用模块并更名： import A as shorter_name
# 调用A中的函数时需要使用A.function()  / shorter_name.function()
# 调用特定函数： from module_name import funciton_name1, function_name2, function_name3
# 调用并更名： from module_name import function_name as new_function_name

import function as f
f.show('Liu', 30, 'Harry Potter')