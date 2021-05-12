lst=[10,20,30,40,50]
print(lst,id(lst))
lst.append(60)
print(lst,id(lst))

lst2=['hello','world']
# lst.append(lst2) #将lst2列表作为一个元素添加到lst中
print(lst)

lst.extend(lst2) #向列表末尾添加多个元素 连接两个列表
print(lst)
lst.insert(1,99) #在任意位置上添加一个元素
print(lst)
lst3=['g','h','j']
#lst[1:]=lst3 #切片 替换
lst.remove(99) #一次移除一个元素 如果有重复移除第一个
print(lst)
lst.pop(1)#根据索引移除一个 元素

print(lst)

lst[1:6]=[]
print(lst)

lst.clear() #清空 列表
print(lst)
#del lst # 删除列表
print(lst)

#修改列表值
lstnew=[10,20,30]
lstnew[1]=100
print(lstnew)
