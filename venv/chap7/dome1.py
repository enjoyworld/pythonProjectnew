#模块

def fun():
    pass
def fun2():
    pass

class Student():
    native_place='shanghai' #类属性
    def eat(self):
        print('eat food')
    @classmethod  #类方法
    def cm(cls):
        pass
    @staticmethod #静态方法
    def sm():
        pass
         
a=10
b=20
print(a+b)