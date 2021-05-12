try:
    a=int(input('请输入第一个整数：'))
    b= int(input('请输入第二个整数：'))
    req=a/b
except BaseException as e:
    print('出错了',e)
else:
    print('结果为',req)
finally:
    print('无论程序是否异常都会执行的代码')
print('程序结束')  