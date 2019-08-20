# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
#
# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
L = list(range(1, 11))
print(L)

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：

L2 = []
for x in range(1, 11):
    L2.append(x * x)

print(L2)

# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环
L3 = [x * x for x in range(1, 11)]
print(L3)

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
L4 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L4)

# 还可以使用两层循环，可以生成全排列：
L5 = [m + n for m in 'ABC' for n in "XYZ"]
print(L5)

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os

L6 = [d for d in os.listdir('.')]
print(L6)
L6 = [d for d in os.listdir('d:/aizp/dev/project/python')]
print(L6)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：

dt = {"x": "a", "y": 'b', 'z': "c"}
for k, v in dt.items():
    print(k, v)
# 因此，列表生成式也可以使用两个变量来生成list：
L7 = [k + '=' + v for k, v in dt.items()]
print(L7)

# 最后把一个list中所有的字符串变成小写：
L8 = ["Hello", 'I', 'Want', "Fly"]
print(L8)
L8 = [s.lower() for s in L8]
print(L8)
