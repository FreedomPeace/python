# 定义可变参数的函数

# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的
# 参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

# 要定义出这个函数，必须确定输入的参数。由于参数个数不确定，我们首先可以想到
# 把a, b, c, ......作为一个list或tuple传进来，这样，函数可以定义如下：

def calc(numbers):
	sum = 0
	for n in numbers:
		sum += n*n
	return sum
# 但是在调用的时候，需要先组装出一个list或tuple:

print(calc([1, 2, 3]))

# 利用可变参数，调用函数的方式可以简化成这样：
# print(calc(1, 2, 3))
# 所以，我们把函数的参数改为可变参数：

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n*n
	return sum
print(calc(1, 3, 5))

# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
# 但是，调用该函数时，可以传入任意个参数，包括0个参数：

print(calc(1, 2))
print(calc())

# 如果已经有一个list或者tuple,要调用可变参数怎么办？可以这样做：
nums = [1, 2, 4]
sum = calc(nums[0], nums[1], nums[2])
print(sum)

# 这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，
# 把list或tuple的元素变成可变参数传进去

print(calc(*nums))

# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法很有用，而且很常见。

# 关键字参数

# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数调用时自动组装为
# 一个dict。请看示例：

def person(name, age, **kw):
	print('name', name, 'age', age, 'other', kw)

person('cqk',19)
person('cqk', 18, city='HeBei')
 
# 关键字参数有什么用？它可以扩展函数的共嫩。比如，在person函数里，我们保证
# 能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能接收
# 到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填向外，其他都是可选项，
# 利用关键字参数来定义这个函数就能满足注册的需求。

# 和可变参数类似，也可以先组装出一个dict，然后，把dict转换为关键字参数传进去：

extra = {'city':'BeiJing', 'job':'Engineer'}
person('lucy', 19, city= extra['city'], job = extra['job'])

# 当然上面的调用可以简写成：
extra = {'city':'BeiJing', 'job':'Engineer'}
person('lucy', 19,**extra)


	




