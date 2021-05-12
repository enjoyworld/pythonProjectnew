#重写
class Person(object):
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def info(self):
        print(self.name,self.age)


class Student(Person):
    def __init__(self,name,age,stu_no):
        super(Student, self).__init__(name,age)
        self.stu_no=stu_no
    def info(self):
        super(Student, self).info()
        print(self.stu_no)

class Teacher(Person):
    def __init__(self,name,age,teachofyear):
        super(Teacher, self).__init__(name,age)
        self.teachofyear=teachofyear
    def info(self):
        super(Teacher, self).info()
        print(self.teachofyear)
stu1=Student('张三',20,100)
teacher=Teacher('李四',22,1001)

stu1.info()
teacher.info()