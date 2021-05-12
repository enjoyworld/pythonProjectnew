for i in range(1,4):
    for j in range(1,5):
        print("*",end='\t')
    print() #换行

for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j, '=',i*j, end=' ')
    print()