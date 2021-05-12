#字符串的大小写转换
s='hello,python'
a=s.upper() #转换为大写 产生一个新的字符串对象
print(a,id(a))
print(s,id(s))

print(s.lower(),id(s.lower()))#产生一个新的字符串对象

s2='hello,Python'
print(s2.swapcase()) #大变小 小变大
print(s2.capitalize()) #第一个字符变大写 其余都小写
print(s2.title()) #每个单词的第一个字母变成大写，单词剩余变成小写

'''字符串对齐'''
s3='hello,World'
print(s3.center(20,'*'))
print(s3.ljust(20,'*')) #左对齐
print(s3.rjust(20,'*'))
'''字符串的分割'''
s4='hello world python'
spl=s4.split()
print(spl)
s5='hello|world|python'
print(s5.split(sep='|'))
print(s5.split(sep='|',maxsplit=1))
'''rsplit()右侧分割'''
print(s4.rsplit())
print(s5.rsplit(sep='|',maxsplit=1))