import time
import  urllib.request
print(time.time())
print(time.localtime(time.time()))
print(type(urllib))
print(type(urllib.request))
print(type(urllib.request.urlopen))
print(urllib.request.urlopen('http://baidui.com').read( ))