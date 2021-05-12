#判断字符串的方法
s='hello,world,python'
print('1.',s.isidentifier()) #flase
print('2.','hello'.isidentifier()) #True
print('3.','张三'.isidentifier())#True



print('4.','abc'.isalpha()) #是否全部由字母组成
print('5.','小王'.isalpha()) #true
print('6.','张三111'.isalpha()) #False

print('7.','1112234'.isdecimal()) #判断字符串是否全部由十进制组成
print('8','111二'.isdecimal()) #false

print('9.','1112234'.isnumeric()) #判断字符串是否全部由数字组成
print('10','111二'.isnumeric()) #ture
print('11','111玩'.isnumeric()) #false

print('12','111qwer'.isalnum()) #是否全部由字母和数字组成
print('13','张三123'.isalnum())
print('14','qwe123!'.isalnum()) #false