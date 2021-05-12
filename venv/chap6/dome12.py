

class Person(object):
    def __init__(self,name,age):
        print('__init__被调用，self的值为：{0}'.format(id(self)))
        self.name=name
        self.age=age
    def __new__(cls, *args, **kwargs):
        print('__new__被调用执行了，cls的id值为:{0}'.format(id(cls)))
        obj=super().__new__(cls)
        print('创建的对象id为:{0}'.format(id(obj)))
        return obj

print('object找个类对象的id是:{0}'.format(id(object)))
print('Person找个类对象的id是:{0}'.format(id(Person)))
stu=Person('马同学',25)
print('stu这个Person类的实例对象的id是:{0}'.format(id(stu)))