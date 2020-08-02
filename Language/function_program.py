# -*- coding:utf-8 -*-
from functools import reduce

ans1 = abs(-1)
fun1 = abs
ans2 = fun1(-1)
print(str(ans1) +'  ' + str(fun1) + '  ' + str(ans2))
#这个例子表明python中不仅函数的结果可以赋给变量，函数名也可以赋给变量,且具有同样的函数效果
#函数名实际是指向函数地址的变量

def addAbs(a, b, functionName):
    return functionName(a) + functionName(b)
ans3 = addAbs(-1, -9, fun1)
print(ans3)

#map/reduce
##map
list1 = [1, -2, 3, -4, 5, -6]
list2 = list(map(fun1, list1))#map返回的是一个map object，还不是list
print(list2)
##reduce
def transform(num1, num2):
    return 10 * num1 + num2
ans4 = reduce(transform, list2)
print(ans4)

#filter
def saveOdd(num):
    return num % 2 == 1
ans5 = list(filter(saveOdd, list2))#同样的filter返回的也是一个filter object，需要list()转换
print(ans5)

#sorted
ans6 = sorted(list1)
ans7 = sorted(list1, key=fun1)
print(ans6)
print(ans7)

#返回函数
def lazySum(*num):#可变参数传入求和数字
    def sum():
        sum = 0
        for x in num:#内部函数sum调用了外部函数lazySum的局部变量num，这种结构称为闭包
            sum = sum + x
        return sum
    return sum
fun2 = lazySum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)#每调用一次lazySum函数就返回一个新的sum函数对象，即使传入的参数相同
ans8 = fun2()#调用lazySum返回的函数
print(ans8)

#lambda表达式
lambda x: x * x
# 等价于
# def f(x):
#     return x * x
ans9 =list(map(lambda x: x * x, list1))
print(ans9)