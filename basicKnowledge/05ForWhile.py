names = ['lily', 'lucy', 'jake']
for name in names:
    print(name)
#     求1+2+...+10的和   --range(10)
total = 0
for x in range(11):
    total += x
    # print(total)

print('1-10的和total为：' + str(total))

nums = [1, 3, 5]
totals = sum(nums)
print(totals)

totals = sum(list(range(101)))
print("100以内的和为：" + str(totals))

totals = 0
x = 99
while x > 0:
    totals = totals + x
    x -= 2
print("100以内奇数和为：" + str(totals))

totals = 0
i = 2
while i < 101:
    totals = totals + i
    i = i + 2
print("100以内偶数和为：" + str(totals))


