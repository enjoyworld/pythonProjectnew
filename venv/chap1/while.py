Sum=0
a=1
while a<=4:
    Sum+=a
    a+=1
print(Sum)
"""计算一到一百的偶数和"""
sum1=0
i=1
while i<=100:
    if i%2==0:
        sum1+=i

    i+=1
print(sum1)
b=sum(range(2,101,2))
print(b)