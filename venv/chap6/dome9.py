# object 类
class Student(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return '名字是{0},年龄{1}'.format(self.name,self.age)

stu=Student('马xx',25)
print(dir(stu))
print(stu)
print()

class Test(object):
    pass
test=Test()
print(test)
