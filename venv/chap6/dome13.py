#类的浅拷贝与深拷贝

class Cpu:
    pass
class Disk:
    pass
class Computer:
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk

cpu1=Cpu()
cpu2=cpu1
print(cpu1)
print(cpu2) #同一内存地址

#（2）类的浅拷贝
print('--------------------------------')
disk=Disk() #创建一个硬板类的对象
computer=Computer(cpu1,disk) #创建一个计算机类的对象

import copy
computer2=copy.copy(computer)
print(computer,computer.cpu,computer.disk)
print(computer2,computer2.cpu,computer2.disk)

#(3) 类的深拷贝
print('-------------------------------------')
computer3=copy.deepcopy(computer)
print(computer,computer.cpu,computer.disk)
print(computer3,computer3.cpu,computer3.disk)