
def fun(arg1,arg2):
    print('arg1',arg1)
    print('arg2',arg2)
    arg1=100
    arg2.append(40)
    print('arg1',arg1)
    print('arg2',arg2)


n1=10
n2=[10,20,30]
print(id(n1))
print(id(n2))

print(n1)
print(n2)

fun(n1,n2)

print(n1)
print(n2)
print(id(n1))
print(id(n2))

""" 在函数调用过程中 进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值
如果是可变对象，在函数体的修改会影响实参的值
"""

