lst=[10,22,4,40,5]
print('排序前',lst,id(lst))
lst.sort()
print('后',lst,id(lst)) #原列表基础上进行排序 默认升序

lst.sort(reverse=True) #降序
print(lst)

print('--------------使用内置函数sorted（）对列表进行排序 会产生新的列表对象----------')
new_lst=sorted(lst)
print(lst)
print(new_lst)
lst2=[i*2 for i in range(1,10)] #列表生成
print(lst2)
lst3=[i for i in range(1,11,2)]
print(lst3)