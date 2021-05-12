s='中国汉字'
print(s.encode(encoding='GBK')) #GBK编码格式中 一个中文占两个字节
print(s.encode(encoding='UTF-8')) #在UTF-8 编码格式中 一个中文站三个字节

#解码
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))

byte1=s.encode(encoding='UTF-8')
print(byte1.decode(encoding='UTF-8'))