#字符串的切片 不可变类型 不具备增删改操作 切片后都产生新的对象
s='hello,python'
s1=s[:5]
s2=s[6:]
s3='!'
newstr=s1+s3+s2
print(s1)
print(s2)
print(newstr)



print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))

print('-----------切片[start:end:step]')
print(s[0:5:1])