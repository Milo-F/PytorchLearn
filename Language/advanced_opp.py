#__slots__
class Student():
    __slots__ = ('name', 'age')#限制给类绑定属性的名称，对子类无效
class Milo(Student):
    pass
milo = Student()
milo.name = 'Milo'
milo.age = 22
i = Milo()
i.score = 98#子类实例可以添加score属性
# milo.score = 98因为__slots__中没有score变量，所以会报错