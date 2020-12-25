# for循环
Name_List = ["Alibaba", "Lucy", "David", "Fion"]
for name in Name_List:
        print(f"{name.upper()}, that was a great idea!")
        print(f"Thaks a lot, {name.upper()}.\n")
print("That was a great discussion everyone.\n")

# exercise 4-2
Animal_List = ["panda", "cat", "tiger", "lion"]
for animal in Animal_List:
    print(f"A {animal.title()} would make a great pet.")
print("\nAny of these animals would make a great pet!")

# range(a,b)生成一个序列，注意b是截止处，不含该数值
for value in range(1,6):
    print(value)

print("\nnow make a list with the range from 1 to 6")
nums = list(range(1,7))
print(nums)
print("\nnow make a list with the range from 1 to 6 with 2 gap")
nums_2 = list(range(1,7,2))
print(nums_2)

print("\nnow calculate x^2 (x = range(1,11))")
squares = []
for value in range(1,11):
    #square = value ** 2
    #squares.append(square)
    squares.append(value**2)

print(squares)
print(f"the minimum number in squares is {min(squares)}.")
print(f"the maximum number in squqres is {max(squares)}.")
print(f"the total number in squares is {sum(squares)}.")

# 直接创建循环数列（合并for和内部的append语句）
list2 =  [value**2 for value in range(1,11)]
print(list2) 

# exercise 4-3
for num in range(1,21):
    print(num)

# exercise 4-5
list_5 = [value for value in range(1,21)]
print(min(list_5))
print(max(list_5))
print(sum(list_5))

# exercise 4-6
list_6 = [value for value in range(1,21,2)]
print(list_6)
length = len(list_6)
print(length)
for num in list_6:
    print(num)

# exercise 4-7
list_7 = [value for value in range(3,31,3)]
for num in list_7:
    print(num)

# exercise 4-8
list_8 = [value**3 for value in range(1,11)]
for num in list_8:
    print(num)

# list[a:b]索引从第a到b位的数值（不含b）
list_9 = list(range(1,11))
print(list_9[2:5])
print(list_9[3:])
print(list_9[-3:])

# 复制切片
my_num = [5, 21, 8]
jack_num = my_num[:]
print("\nMy favorite nums are:")
print(my_num)
print("\nJack's favorite nums are:")
print(jack_num)

my_num.append(36)
jack_num.append(26)
print("\nMy newest favorite num is:")
print(my_num[-1])
print("\nJack's newest favorite num is:")
print(jack_num[-1])

# 元组是不可变的列表，用()定义，而不是[]
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 50
# 由于dimensions是元组，所以不可修改值，会报错

# exercise 4-13
food_list = ("apple", "cake", "meat", "noodles", "pizza")
for food in food_list:
    print(food)

# food_list[0] = "pear"
food_list = ("pear", "cake", "vegetables", "noodles", "pizza")
for food in food_list:
    print(food)