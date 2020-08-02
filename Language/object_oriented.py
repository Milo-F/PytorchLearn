# 通过class定义类，括号内表示类的继承父类
class Student(object):
    # self表示创造的实例本身，所以通过__init__方法，可以将name、age等属性传递给实例
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__()
    # 在类中定义的方法，第一个参数只能是self
    def printInfo(self):
        print(self.name, self.age)
    pass
#根据类名创造实例
milo = Student('milo', 22)
# 可以自由地给实例绑定属性，即使是类中没有的属性
milo.num = 1
print(milo.num, milo.name, milo.age)
milo.printInfo()# 调用时不用手动传入self参数内容

# 访问限制
class Student_1():
    def __init__(self, name, age):
        # 通过在成员变量名字之前加两个下划线，将变量设置为private。
        self.__name = name
        self.__age = age
        super().__init__()
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
july = Student_1('July', 18)
# print(july.__name)外部方法不能访问内部私有变量
july.set_age(16)
print(july.get_name(), july.get_age())#只能通过类内部方法访问成员变量
print(july._Student_1__name)#解释器将__name改为了_Student_1__name，但是不要这么做

# 继承和多态
class Animal():
    def __init__(self):
        super().__init__()
    def run(self):
        print('running')
# Dog类继承了Animal类，即使什么都没做，仍可以使用Animal的run方法
class Dog(Animal):
    pass
# Cat类继承了Animal类，但是重写了run方法，还新增了Cat独有的内容eat方法
class Cat(Animal):
    def run(self):
        print('cat is running')
    def eat(self):
        print('cat is eating')
dog = Dog()
dog.run()
cat = Cat()
cat.run()
cat.eat()
# 在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行(多态)
# 多态的好处在于当我们需要接收同一继承关系的不同子类对象时，只需要声明接收其父类对象即可传入所有子类对象
# 对扩展开放：允许新增子类；
# 对修改封闭：不需要修改依赖父类的方法。

# 获取对象信息
# 判断实例是否属于类：isinstance()
print(isinstance(dog, Dog), isinstance(cat, Dog), isinstance(dog, Animal))
# 获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list
print(dir(cat))