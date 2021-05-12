#多态
class Animal(object):
    def eat(self):
        print('动物吃什么')

class Cat(Animal):
    def eat(self):
        print('猫咪爱吃鱼')

class Dog(Animal):
    def eat(self):
        print('狗狗爱吃骨头')
class Person:
    def eat(self):
        print('人什么都吃')

def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())

fun(Person())