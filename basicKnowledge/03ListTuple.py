classmates = ['lucy', 'lose', 'jake']

print(classmates)

print(len(classmates))

print(classmates[0])
print(classmates[1])
print(classmates[2])
# IndexError: list index out of range
# print(classmates[4])
print(classmates[-1])

print(classmates)
print('在list集合最后添加一个元素')
classmates.append(66)
print(classmates)

print('add a element at a index location of list')
classmates.insert(1, 1)
print(classmates)

classmates.pop()
print(classmates)

classmates.pop(1)
print(classmates)

# tuple是另一种有序列表叫元组，一旦初始化就不能修改；比如同样是列出同学的名字
print('tuple是另一种有序列表叫元组，一旦初始化就不能修改；比如同样是列出同学的名字')
schoolFriend = ('jake', 'rose', 'lucy')
print(schoolFriend[0])
print(len(schoolFriend))
# 'tuple' object does not support item assignment
# schoolFriend[0] = 66
