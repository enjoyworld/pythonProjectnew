s={10,20,30,40}
s2={40,20,30,10}
'''两个集合是否相等 看元素是否相同'''
print(s==s2)
print(s!=s2)

'''一个集合 子集关系'''
s1={10,20,30,40,50,60}
s2={40,20,30,10}
s3={10,20,3333}
print(s2.issubset(s1)) #true
print(s3.issubset(s1)) #false
''' 一个集合是否是里一个集合的超集'''
print(s1.issuperset(s2))
print(s1.issuperset(s3))

'''两个集合是否有交集'''
print(s2.isdisjoint(s1)) # isdisjoint不相交 返回false 表示有交集

'''集合的数学操作'''
print(s1.intersection(s2)) #取交集
print(s1 & s2 )

"""并集"""
print(s1.union(s2))# 取并集 union
print(s1 | s2)

'''差集'''
print(s1.difference(s2))
print(s1-s2)

'''对称差集'''
print(s2.symmetric_difference(s1))
print(s2^s1)

