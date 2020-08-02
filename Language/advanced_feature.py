# -*- coding:utf-8 _*-

#切片, slice
name = ['milo', 'lily', 'tom', 'jerry', 'jack']
print(name[:3])#n:m表示从索引n开始直到m（但是不包括m）若第一个索引是0可省略
print(name[-3:])#切片操作同样支持负数索引。
num = list(range(100))
print(num[:50:10])#前50个数，每10个取一次

#迭代，利用for循环遍历
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)

#列表生成式
l1 = [x * x for x in range(10)]#生成元素为x*x的列表
l2 = [x*x for x in range(10) if x%2 == 0]#还可以加判断
l3 = [m+n for m in 'ABC' for n in 'DEF']#还可以多重循环嵌套
l4 = [x if x%2 == 0 else -x for x in range(10)]#带else的if需要给定具体的X或else中的值，以供for使用，要放前面
print(l1)
print(l2)
print(l3)
print(l4)

#生成器，将列表生成器的[]改为()即创建一个generator，保存的是算法（x*x）仅在使用的时候调用计算
g1 = (x*x for x in range(10))
for n in g1:
    print(n)
def odd():#方法定义generator，yield起到return的作用，每次调用方法都从上次返回的yield处继续执行
    print('step1')
    yield 1
    print('step2')
    yield 3
    print('step3')
    yield 5
g2 = odd()
print(next(g2))
print(next(g2))
print(next(g2))

#迭代器，可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。