class Student(object):
    # __slot__ 关键字
    pass
# 尝试给一个实例绑定一个属性
s = Student()
s.name = 'python'
print(s.name)

# 还可以尝试给实例绑定一个方法
def set_age(self, age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s) # 给实例绑定一个方法
s.set_age(23) #调用实例方法
print(s.age)

# 但是，给一个实例绑定方法，对另一个实例是不起作用的
s2 = Student()
#s2.set_age(22)
#print(s2.age)
# 为了给所有实例都绑定方法，可以给class绑定方法
def set_score(self,score):
    self.score = score

Student.set_score = set_score
s.set_score('88')
print(s.score)

# 使用__slots  限制实例的属性
class Student2(object):
    __slots__ =('name', 'age') #用tuple定义允许绑定的属性名称
s3 = Student2()
s3.name = 'jack'
s3.age = 33
#s3.score = 89
#print(s3.score)
# 使用__slots__要注意，__slots__定义的属性仅对当前实例起作用，对继承的子类是不起作用的:
class GraduateStudent(Student2):
    pass
g = GraduateStudent()
g.score = 99
print(g.score)
