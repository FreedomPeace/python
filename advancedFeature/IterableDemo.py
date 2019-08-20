#  迭代

# python中迭代是通过for  in 结构来实现,不仅list和tuple 可以迭代，dict也可以迭代
from collections import Iterable

L = [1, 2, 5, 8]
for n in L:
    print(n)
print('==========')

T = ('1', 'a', 'b')
for t in T:
    print(t)


print('====默认是获取dict字典的key======')
Dt = {'name': 'aizp', 'age': 18, 'gender': 'm'}
# 默认是获取dict字典的key
for dt in Dt:
    print(dt)
print('====获取字典的值======')
for dt in Dt.values():
    print(dt)

print('====获取字典的key和word======')
for dt in Dt.items():
    print(dt[0], dt[1])
    print(dt)

print('======迭代字符串abcd======|')
for s in 'abcd':
    print(s)

print('======判断一个对象是否是迭代对象======|')

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))



