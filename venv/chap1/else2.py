a=0
while a<3:
    pwd=input("please input your password")
    if pwd=="888":
        print("password correct")
        break
    else:
        print("password wrong")
    a+=1
else:
    print("no opportunity")

