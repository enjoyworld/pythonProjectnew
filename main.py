# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import sys
from sys import argv,path
from random import  random
str="hello word"
a="h"
#print(str*2)
# 字符串 print(str[1:2])
'''for i in str:
    print(i)
'''
# if
'''if a in str:
    print("Ture " + "a="+a)
else:
    print("False")'''
# 换行输出
#x="a"
#y="b"
#print(x,end=" ")
#print(y,end=" ")
'''print("===============python import test ==========")
print('cmd input:')
for i in sys.argv:
    print(i)
print('Path:',path)'''

# a=b=c=1
'''a=1
b=5.5
c="www.alis.com"
d=[1,2,"cat"]
e={"dog":"狗"}
f=(1,2,3,4)
print(type(a),type(b),type(c),type(d),type(e),type(f))
d[0]=9
print(d[0:3])
print(f[0:2])
print("=================-----==============")
ran = random()
print(ran)
print("\a")
# 格式化 字符串
print("我是%s，今年%s岁" % ("王权但",20))
'''
# 斐波那契数列
a,b = 0,1
while b < 10:
    print(b, end=" ")
    a, b = b, a+b

for i in range(0,100, 10):
    print(i)

hi=['beijing', 'shanghai','nanjing']
for e in range(len(hi)):
    print(e,hi[e])
 list1 = [1,2,3,"w",5]
it=iter(list1)
for i in list1:
    print(i,end=" ")
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
