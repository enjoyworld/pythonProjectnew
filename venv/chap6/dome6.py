#面对对象的 三大特征
'''
封装：提高程序的安全性
继承：提高代码复用性
多态：提高程序的可扩展性和可维护性
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def show(self):
        print(self.name,self.__age)

stu1=Student('小王吧',20)
stu1.show()
Student.show(stu1)
print(stu1.name)
#print(dir(stu1))
print(stu1._Student__age)