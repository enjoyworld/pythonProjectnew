
def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)

#函数调用
fun(10,20,30)
lst=[10,20,30]
#fun(lst)
fun(*lst) #在函数调用时 将列表每个元素转换为位置实参传入

fun(a=1,b=2,c=3)

dic={'a':100,'c':200,'b':300}
#fun(dic)
fun(**dic)