# def my_abs(x):
#     if x > 0:
#         return x
#     else:
#         return -x
#
#
# z = my_abs(-9)
# print(z)
#
# TypeError: '>' not supported between instances of 'str' and 'int'
# print(my_abs('a'))
import math


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


# print(my_abs('22'))
print(my_abs(-9))


def quadratic(a, b, c):
    #print(b)
    x1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 / a
    x2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 / a
    return x1, x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def null_fuc():
    """
    定义空函数通过pass关键

    pass语句什么都不做，那有什么用？
    实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，
    就可以先放一个pass，让代码能运行起来。

    pass还可以用在其他语句里，比如：

    if age >= 18:

    pass
    """
    pass

null_fuc()

def null_fun2():
	#age is str 
	age = input('请输入你的年龄:') 
	if int(age) >= 18:
		print('adults')
	else:
		#print('children')
		pass
		
null_fun2()		
