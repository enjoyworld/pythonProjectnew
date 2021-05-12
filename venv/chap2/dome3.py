#元组的创建 不可变的
t=('w',1,'apple',99)
t='w',1,'apple',99
t3='python',
print(type(t3))
print(t3)
print(t)
print(id(t))
t1=tuple(('w',1,'apple',99))
print(t1)
print(id(t1))

lst=[]
lst1=list()

d={}
d2=dict()

t4=()
t5=tuple()
print('空列表',lst,lst1)
print('空字典',d,d2)
print('空元组',t4,t5)