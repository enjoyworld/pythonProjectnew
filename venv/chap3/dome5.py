#字符串的替换
s='hello,Python'
print(s.replace('Python','java'))
s1='hello,python,python,python'
print(s1.replace('python','java',2))

lst=['hello','java','python']
print('|'.join(lst))

t=('hello','java','python')
print(' '.join(t))

print('*'.join('python'))