

def fun(num):
    odd=[]
    even=[]
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

#函数的调用
lst=[10,20,25,6,3,5,9,77,85]
print(fun(lst))
'''
函数的返回值
1 如果函数没有返回值 return 可以不写
2 函数的返回值，如果是一个，直接返回类型
3 函数的返回值 如果是多个 返回一个元组
'''