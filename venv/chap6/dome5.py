

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eat(self):
        print(self.name+'在吃饭')

stu1=Student('张三',30)
stu2=Student('李四',40)
stu1.eat()
stu2.eat()

print('-------stu2动态绑定性别属性')
stu2.gender='女'
print(stu1.name,stu1.age)
print(stu2.name,stu2.age,stu2.gender)

def show():
    print('定义在类之外的，称函数')

stu1.show=show
stu1.show()