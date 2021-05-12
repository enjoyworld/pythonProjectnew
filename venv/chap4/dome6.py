
def fun(a,b,*,c,d): #从这*之后 函数调用时 只能采用关键字传参
    print('a=',a)
    print('b=', b)
    print('c=', c)
    print('d=', d)

#fun(10,20,30,40)

fun(a=10,b=20,c=30,d=40)

fun(10,20,c=30,d=40)


