# -*- coding:utf-8 -*-

#调用函数
abs(-100)

#定义函数
def compare(a, b):
    if a > b:
        return a, b
    elif a < b:
        return b, a
    else:
        return 0
print(compare(10, 20))#函数返回多个值本质是返回一个tuple

#函数的参数
##默认参数
def getSum(n = 2):
    sum = 0
    for i in range(0, n):
        sum = sum+i
    return sum
print(getSum(n = 10))
##可变参数
def getMean(*num):
    result = 0
    for i in range(0, len(num)):
        result = result+num[i]
    result = result/len(num)
    return result
print(getMean(1, 2, 3, 4, 5))
##关键字参数
def usrInfo(name = '', **info):
    print(name, info)
usrInfo('milo', age = 22, sex = 'male')
info = {'age':14, 'sex':'male'}
usrInfo('lily', **info)
##命名关键字参数
def _usrInfo(name, *, age = 0, sex = 'None'):
    print(name, age, sex)
usrInfo('milo', age = 22)
