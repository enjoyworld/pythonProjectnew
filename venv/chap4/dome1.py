
# 函数 复用代码 隐藏实现细节 提高可维护性 提高可读性便于调试

def calc(a,b): #a b 为形参数 出现在函数的定义处
    c=a+b
    return c

result=calc(10,22) # 10 22 实际参数值 简称 实参 函数的调用处
result1=calc(b=10,a=22)
print(result)
print(result1)

