# 类

class Student:  #Student 由一个或多个单词组成，每个单词首字母大写其余小写
    native_pace='安徽' #直接写在类里的变量，称为类属性

    def __init__(self,name,age):
        self.name=name
        self.age=age

    #实例方法
    def eat(self):
        print('干饭人 干饭混 一顿不吃没精神')

    #静态方法
    @staticmethod
    def method():
        print('我使用了@staticmethod修饰 这里是叫做 静态方法 不带self ')
    #类方法
    @classmethod
    def cm(cls):
        print('我是类方法 ')

#在类之外定义的叫函数 类里面叫方法
