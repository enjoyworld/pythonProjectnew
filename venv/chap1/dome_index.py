lst=['one','two',3,'one','ww',6]
print(lst.index("one"))#如果列表中有相同元素 直返第一个元素索引
print(lst.index('one',1,5))
#------------
print(lst[3])
print(lst[-1])
print("------------切片---------")
lst2=lst[1:3:1] #左闭右开

print(lst2)
print(id(lst))
print(id(lst2))
print(lst[::-1])