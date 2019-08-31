def normalize(name):
    normalName = ""
    if isinstance(name, str):

        num = 0
        for n in name:
            if num == 0:
                normalName += n.upper()
            else:
                normalName += n.lower()
            num += 1
    return normalName


L1 = ['adam', 'LISA', 'barT']
print(list(map(normalize, L1)))

from functools import reduce
from collections import Iterable


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    if not isinstance(L, Iterable):
        print("is not a iterable obj")
        return

    return reduce(lambda x, y: x * y, L)


print(prod(33))
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
