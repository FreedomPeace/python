names = ['lily', 'lucy', 'jake']
ages = [18, 12, 13]

d = {'lily': 18, 'lucy': 12, 'jake': 12}

fromkeys = d.fromkeys(names)
print(fromkeys)

# 把list集合作为新生成字典的keys,并赋予默认值66
fromkeys = dict.fromkeys(names, 66)
print(fromkeys)

# 获取字典对象所有的key
keys = d.keys()
print(keys)

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['luck'] = 88

# 第一种方式，获取value
print(d['lucy'])
# 如果key不存在字典d中，则会报错 KeyError: 'luck'
try:
    print(d['luck'])
except KeyError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# 第二种方式，获取key对应的value
# 根据key获取对应的value，如果key不存在，则返回none或者定义的默认值
print(d.get('lucy'))
print(d.get('luck', -1))

d.pop('lucy')
print(d)
# dict end

# set start
# set和dict类似，也是一组key的集合，但不存value。由于key不重复，所以在set中，没有重复的key
s = {1, 2, 3}
print(s)
li = [1, 3, 5, 7, 7, 5, 3]
s = set(li)
print(s)

s.add(9)
print(s)

s.remove(9)
print(s)

s.pop()
print(s)

print('可以看成数学意义里的无序和无重复元素的集合，因此可以做数学上的交集，并集等操作')
s1 = {1, 2, 3, 4}
s2 = set([2, 3, 5])
print("s1:"+str(s1))
print("s2:" + str(s2))
print("s1&s2:" + str(s1 & s2))
print('s1 | s2:' + str(s1 | s2))

# TypeError: unhashable type: 'list'
sss = {names, 2, 3, 8}
print(sss)
