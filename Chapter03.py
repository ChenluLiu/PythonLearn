
# []表示列表
color = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]
print(color)
print(color[0])
print(color[6])
print(color[6].title())
print(color[6].upper())

# -1为索引最后一项
print(color[-1])

message = f"\nmy favorite color is {color[2]}."
print(message)
print(message.title())

# 变更列表内项目
message_2 = '''\nnow change the firt item in color to "change"''' 
print(message_2.title())
color[0] = "change"
print(color)

# append()在末尾添加新项
message_3 = '''\nnow add "bird" in color'''
print(message_3.title())
color.append("bird")
print(color)

# 创建新表
message_4 = "\nnow create a new item list"
print(message_4)
item = []
print(item)
item.append("chair")
print(item)
item.append("desk")
print(item)

# insert(a,b)在a序列插入元素b
message_5 = "\nnow insert 'bed' into the item list between chair and desk"
print(message_5)
item.insert(1,"bed")
print(item)

# del语句删除a序列元素
message_6 = "\nnow delete desk"
print(message_6)
del item[2]
print(item)

# pop()删除指定位置元素，默认为末尾
print("\nnow add a new motorcycle list")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)
print("\nnow use pop() to delete the last item")
poped_motorcycles = motorcycles.pop()
print("\nnow the list is:")
print(motorcycles)
print("\nthe deleted item was:")
print(poped_motorcycles)
print("\nnow delete the first item")
first_item = motorcycles.pop(0)
print(motorcycles)

# remove()删除指定值的元素,只删除第一个。有重复时使用循环来删除全部
print("\nnow remove yamaha from the list")
motorcycles.remove("yamaha")
print(motorcycles)

# sort()进行永久排序,reverse=true反向排序
cars = ["bmw", "benz", "audi", "toyota"]
message_7 = f"\n{cars}"
print(message_7)
print("\nnow sort the list")
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sorted()进行临时排序
cars = ["bmw", "benz", "audi", "toyota"]
message_7 = f"\n{cars}"
print(message_7)
print("\nnow sorted the list")
print(sorted(cars))
print(sorted(cars,reverse=True))
print("\nthe original list is")
print(cars)

# reverse()元素倒序
print("\nuse reverse to the followed list")
print(cars)
cars.reverse()
print(cars)

# len()确定列表长度
num = len(cars)
print("\nthe length of the car list is:")
print(num)
