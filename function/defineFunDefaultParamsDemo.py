#我们先写一个计算x2的函数：

#def power(x):
#	return x * x

#print(power(2))

#现在，如果我们要计算x3怎么办？可以再定义一个power3函数，
#但是如果要计算x4、x5……怎么办？我们不可能定义无限多个函数。
#你也许想到了，可以把power(x)修改为power(x, n)，用来计算xn，说干就干：
#
def power(x , n):
	s = 1
	while n > 0:
		n -= 1
		s *= x
	return s

#对于这个修改后的power(x,n)函数，可以计算任意n次方	
print('power(2,3) = ',power(2,3))	
print('power(2,5) = ',power(2,5))	

#默认参数

#修改后的power(x,n)函数定义没有问题，但是，旧的调用代码失败了，
#原因是我们增加了一个参数，导致旧的代码因为缺少一个参数而无法正常调用：

#power(5)
#>>> power(5)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: power() missing 1 required positional argument: 'n'

#这个时候，默认参数就派上用场了。由于我们经常计算x2,所以，完全可以把第二个参数
# n的默认值设定为2：
def power(x , n = 2):
	s = 1
	while n > 0:
		n -= 1
		s *= x
	return s
#这样我们调用power(5)时，相当于调用power(5,2):
print('power(5) = ', power(5))

def enroll(name, gender, age=6, city='BeiJing'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)

enroll('cqk','M')
enroll('lily', 'F', 22, 'Japan')
enroll('lucy', 'F', 18)
enroll('rose', 'F', city='American')

#默认参数很有用，但使用不当，就会掉入坑里
#演示如下

def add_end(L = []):
	L.append('END')
	return L
#当你调用时，似乎结果不错：
print(add_end([1, 2, 3]))

#当你使用默认参数调用时，一开始结果也是对的：
print(add_end())

#但是，再次调用add_end()时，结果就不对了：
print(add_end())
print(add_end())

#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
#如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

#定义默认参数要牢记一点：默认参数必须指向不变对象来实现：
def add_end(L = None):
	if L is None:
		L = []
	L.append('END')
	return L
#现在无论调用多少次，都不会有问题：
print(add_end())
print(add_end())

#为什么要涉及str、None这样的不变对象呢？因为不变对象一旦创建，
# 对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点
# 问题都没。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


