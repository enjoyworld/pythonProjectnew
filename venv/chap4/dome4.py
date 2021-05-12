#函数参数的定义

def fun(*args): #函数定义  个数可变的位置参数
    print(args)

fun(10)
fun(10,20)  #结果是一个元组


def fun1(**args): # 个数可变的关键字参数 返回字典
    print(args)

fun1(a=10)
fun1(a=10,b=99)

def fun2(*args1,**args2):
    psss