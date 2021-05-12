#递归函数
def fac(n):
    if n==1:
        return 1
    else:
        req=n*fac(n-1)
        return  req

print(fac(10))

#斐波那契数列

def fib(n):
    if n == 1:
        return  1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(6))