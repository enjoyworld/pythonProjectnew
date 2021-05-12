
try:
    a=int(input('请输入第一个整数：'))
    b= int(input('请输入第二个整数：'))
    req=a/b
    print('结果为%f' % req)

except ZeroDivisionError:
    print('对不起 除数不能为零')
print('程序结束')
