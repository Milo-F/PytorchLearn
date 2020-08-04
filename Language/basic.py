# -*- coding:utf-8 -*-

#list and tuple
# list
number_list = ['jw', 'yi', 'by']  # This is a list
print(
    len(number_list),
    number_list[0],
    number_list[1],
    number_list[2],
    number_list[-1],
    number_list[-2]
)
number_list.append('dy')  # 添加元素
print(number_list)
number_list.insert(1, 'insert')  # 指定位置插入元素
print(number_list)
number_list.pop()  # pop函数默认删除最后一个元素
print(number_list)
number_list.pop(1)  # 指定位置删除元素
print(number_list)

# tuple
number_tuple = ('jw', 'yi', 'by')
print(number_tuple)  # tuple 无法修改

##tuple + list
number = (number_tuple, number_list)
print(number)
number[1].append('dy')  # list 作为 tuple 的元素其内容可以修改，但list自身不能变
print(number)

# 分支和循环
# 分支（条件语句）
salary = int(input('input your salary:\n'))
if salary < 5000 and salary >= 0:
    print('low')
elif salary <= 10000:
    print('medium')
else:
    print('high')

# 循环
for num in number_list:
    print(num)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

#dict and set
# dict 和list相比，空间换取时间：查找/插入速度快，内存占用高，key必须是不可变对象
number_dict = {1: 'jw', 2: 'yi', 3: 'by'}
print(number_dict[2])
print(4 in number_dict)  # 判断key 4是否存在
number_dict[4] = 'dy'  # 直接对新key赋值添加
number_dict.pop(1)
print(number_dict)

# set
number_set = set(number_list)
print(number_set)
number_set.add('dy')
number_set.remove('jw')
print(number_set)
