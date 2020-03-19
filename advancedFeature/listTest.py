L1 = ['Hello' , 13 , 'world']
print(L1)
L2 = [ x.lower() for x in L1 if isinstance(x,str) ]
print(L2)
