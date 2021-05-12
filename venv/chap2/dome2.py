#字典元素的获取
#字典 键不可以重复 值可以重复
zd={'one':1,'two':2,'three':3}
print(zd['one'])
print(zd.get('one'))
print(zd.get('five')) #查找的键不存在 返回none 不报错
print(zd.get('five','没有找个键'))

print('one' in zd)
print('one' not in zd)

del zd['one'] #删除指定的 key-value
# zd.clear() 清空
print(zd)
zd['five']=5 #新增一个元素
print(zd)
# 字典视图
print(zd.values())
print(zd.keys())
print(zd.items())
#字典元素遍历
for item in zd:
    print(item,zd[item])
#字典生成式
items=['q','w','e','r']
prices=[1,2,3,4,5,6]

d={item.upper():price for item,price in zip(items,prices)}
print(d)
