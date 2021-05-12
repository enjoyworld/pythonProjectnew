for i in range(3):
    pwd=int(input("请输入密码"))
    if pwd==888:
        print("nice job")
        break
    else:
        print("do it again")
else:
    print("game over")
