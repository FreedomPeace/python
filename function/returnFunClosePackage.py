def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i

        fs.append(f)
    print(fs)
    return fs
f1,f2,f3 = count()
#for i in f1:
#    print(i())
print(f1)
print(f2())
print("直接运行count函数")
print(count())
