s={10,2,25,63}
print(2 in s)
print(11 in s)
print(11 not in s)

'''新增'''
s.add(999)
print(s)
s.update({200,888,555})
print(s)
s.update([1,2,3,9999,88888,525])
print(s)
'''集合元素的删除 remove'''
s.remove(9999)
print(s)
#s.remove(0)
print(s) #抛出异常
s.discard(5656) #不抛出异常
print(s)
s.pop() #随机删除任意一个元素
print(s)
s.clear()#清空
