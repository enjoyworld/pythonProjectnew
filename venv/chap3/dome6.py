#字符串的比较 运算符 >,>=,<,<=,==,!=

print('apple'>'app') #true
print('apple'>'banana')

print(ord('a'),ord('b'))

print(chr(97),chr(98)) #


'''==与is的区别
==比较的是values是否相等
is 比较的是id'''

a=b='python'
c='python'

print(a==b)
print(a==c)

print(a is b)
print(a is c)

print(id(a))
print(id(b))
print(id(c))