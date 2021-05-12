import socket
ip=input('输入主机地址')
port=21
s=socket.socket()
s.connect((ip,port))
req=s.recv(1024)
s.close()
print(req)