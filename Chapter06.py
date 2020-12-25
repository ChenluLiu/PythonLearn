# Chapter 6 {}键

# Exercise 6-1
my_info = {
    "first_name": "Chenlu",
    "last_name": "Liu",
    "age": 30,
    "city": "Beijing",
           }
for i in my_info:
    j = my_info[i]
    print(f"My {i} is {j}.")

# Exercise 6-2
favorite_num = {
    "Jack": 9,
    "Lucy": 28,
    "Maria": 6,
    "Duck": 82,
    "Dan": 20,
    }

for i in favorite_num:
    j = favorite_num[i]
    print(f"{i}'s favorite number is {j}.")

# 用items()遍历字典的键和值，做到同上的功能
print("use items()")
favorite_num = {
    "Jack": 9,
    "Lucy": 28,
    "Maria": 6,
    "Duck": 82,
    "Dan": 28,
    }

for name, num in favorite_num.items():
    print(f"{name}'s favorite number is {num}.")

# 用keys()遍历字典的键
print("use keys()")
for name in favorite_num.keys():
    print(f"{name} is in the system.")
# 在字典里调用默认为全部键，但是用key()更易于理解
for name in favorite_num:
     print(f"{name} is in the system.")

for name in sorted(favorite_num.keys()):
 print(f"{name} is in the system.")

 # 用values()遍历字典的值
print("use values().") 
for num in favorite_num.values():
     print(f"{num} is in the system.")

# 用set集合确保没有重复的值
print("use set()")
for num in set(favorite_num.values()):
    print(f"{num} is in the system.")

# Exercise 6-6
favorite_language = {
    "a": "c",
    "b": "python",
    "c": "java",
    "d": "c",
    "e": "java",
    }

name_list = {'d', 'e', 'f', 'g', 'h'}
for name in name_list:
    if name in favorite_language.keys():
        print(f"{name}, you have done well!")
    else:
        print(f"{name}, please join us!")

# 嵌套
alien_0 = {"color": "red", "points": 5}
alien_1 = {"color": "yellow", "points": 3}
alien_2 = {"color": "green", "points": 1}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 使用range()自动生成空列表
print("use range() to create list")
aliens = []
for alien_num in range(30):
    new_alien = {"color": "green", "points": 1, "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens: {len(aliens)}.")

# 修改前三个为黄色
print("Change the first 3 aliens to yellow.")
for alien in aliens[:3]:
    if alien["color"]  == "green":
        alien["color"] = "yellow"
        alien["points"] = 3
        alien["speed"] = "medium"
    else:
        alien["color"] = "red"
        alien["points"] = 5
        alien["speed"] = "fast"
for alien in aliens[:5]:
    print(alien)

# Exercise 6-9\6-10\6-11
favorite_places = {
    "Lucy": ["Beijing", "Munich",],
    "Jack": ["Nanjing",],
    "Maria": ["Chengdu", "Dalian",],
    "Duck": ["Paris",],
    "Dan": ["NYC",],
    }
for name, places in favorite_places.items():
    print(f"{name.upper()}'s favorite place is:")
    for place in places:
        print(place)
