import  pickle
Str="aaaa"
r=pickle.dumps(Str)
print(r)
a=pickle.loads(r)
print(a)
print(__name__)
if __name__=="__main__":
    filename="F://test.txt"
    txt="hello  word"
    f=open(filename,'w+')
    print(txt,file=f)
    f.close()