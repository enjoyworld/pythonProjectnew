t=(10,[20,30],40)
print(t)
print((type(t)))
print(id(t))

print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

print(id(100))
#t[1]=100
t[1].append(100)
print(t)
print(id(t))

#遍历元组
for i in t:
    print(i)