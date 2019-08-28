
g = (x*x for x in range(10))

for y in g:
    # print(y)
    pass

# def triangles():
#     L = []
#     n = 1
#     while True:
#         L.append(n)
#         n = n + 1
#         yield L
def triangles():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
