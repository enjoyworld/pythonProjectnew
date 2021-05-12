#格式化字符串
# 1 % 占位符
name='张三'
age=20
print('我叫%s，今年%d'% (name,age))

# 2 {}
print('我叫{0}，今年{1}'.format(name,age)) #format 方法

# 3 f-string

print(f'我叫{name},今年{age}岁')

print('---------------拼接------------------------')

print('我叫'+name+' 今年'+str(age))