"""输出1-100  5的倍数"""
for  item in  range(1,101):
    if item%5==0:
        print(item)


print('-----------------------------使用continue-----------')
for i  in range(1,101):
    if i%5!=0:
        continue
    print(i)