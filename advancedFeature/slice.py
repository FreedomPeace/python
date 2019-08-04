# 切片

# 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：

L = ['lily', 'lucy', 'jake', 'rose']

# 取前三，怎么做
# 笨办法：之所以是笨办法是因为扩展一下，取前N个元素就没辙了。
print([L[0], L[1], L[2]])

# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：

r = []
n = 3
for num in range(n):
    r.append(L[num])
print(r)

# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，
# Python提供了切片(Slice)操作符，能大大简化这种操作。

# 对应上面的问题， 取前3个元素，用一行代码就可以完成切片：
print('切片Slice，L[0:3] = ', L[0:3])

# L[0:3] 表示，从索引0开始取，直到索引3为止，但不包含索引3.

# 如果第一个索引是0，还可以省略：
print('切片Slice，L[:3] = ', L[:3])

# 也可以从索引1开始取，取出两个元素
print('切片Slice，L[1:3] = ', L[1:3])

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片

print(L[-2:])  # 从倒数第二个 一直取到最后一个，包括最后一个
print(L[-2:1])
print(L[-2:-1])
