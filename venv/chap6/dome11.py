

class A:
    pass
class B:
    pass
class C(A,B):
    def __init__(self,name,age):
        self.name=name
        self.age=age
x=C('jim',20)
print(x.__dict__)
print(C.__dict__)
