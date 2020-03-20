def isNotEmpty(s):
    return s and s.strip()
L =list(filter(isNotEmpty,["a","",None,"b"]))
print(L)
