age = 88
if age >= 18:
    print("adult")
else:
    print("child")

season = input("请输入你喜欢的季节：(eg:spring,summer,autumn,winter)")
if season == 'spring':
    print("你喜欢春天哦，春天是个万物复苏的季节")
elif season == 'summer':
    print("这是夏天，夏天是有点热哦")
elif season == 'autumn':
    print("这是秋天，秋天是个丰收的日子")
elif season == 'winter':
    print('这是冬天，冬天会下雪哦，特别冷的')
else:
    print('你输入的我无法翻译')

    # 练习
    # 小明身高1
    # .75，体重80
    # .5
    # kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
    #
    # 低于18
    # .5：过轻
    # 18.5 - 25：正常
    # 25 - 28：过重
    # 28 - 32：肥胖
    # 高于32：严重肥胖
