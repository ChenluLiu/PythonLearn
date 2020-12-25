#-------------------
# f字符串：在字符串中加入变量的数值，变量放在{}内
# title() 首字母大写
# upper/lower() 全大写/全小写
#-------------------
first_name = "chenlu"
last_name = "liu"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name}")
print(f"Hello, {full_name.upper()}")
print(f"Hello, {full_name.lower()}")
print(f"Hello, {full_name.title()}")

message = f"try message, {full_name}"
print(message)

# \t 空格
# \n 换行
print("\tThis is a tab")
print("\nThis is a new line")

# rstrip() 去除末尾空白
# lstrip() 去除开头空白
# strip() 去除首尾空白
begin_blank = " ahola!"
end_blank = "ahola! "
both_blank = " ahola! "
print(begin_blank)
print(begin_blank.lstrip())

# exercise 2-5
f_name = " 鲁迅 "
f_speech = "走的人多了就成了路"
sentence = f_name + " once said, " + '''"''' + f_speech + '''"'''
print(sentence)
sentence = f_name.strip() + " once said, " + '''"''' + f_speech + '''"'''
print(sentence)
sentence = f_name.strip() + " once said, \n" + '''"''' + f_speech + '''"'''
print(sentence)

# 用下划线标注大数字,适用于int和float
exp_1 = 1400000
exp_2 = 1_400_000
print(exp_1)
print(exp_2)

# 多变量赋值
exp_1, exp_2 = 15000, 20_000
print(exp_1)
print(exp_2)

# exercise 2-8
# 除法/结果为float，//结果为int
print(3+5)
print(20-12)
print(2**3)
print(16/2)
print(16//2)

# 通常用全大写定义一个不应改变的常量
MY_AGE = 18
print(MY_AGE)

# Python代码原则
import this







