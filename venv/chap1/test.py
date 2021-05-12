import pickle
class test(object):
    def __init__(self,user,password):
        self.user=user
        self.password=password
vstar=test('mzy',123456)
vstar_p=pickle.dumps(vstar)
print(vstar_p)
v=pickle.loads(vstar_p)
print(v.user)
print(vstar.user)
print(v)
print(test)