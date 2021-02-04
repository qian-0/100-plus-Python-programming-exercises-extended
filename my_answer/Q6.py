import math

num = input("请输入逗号隔开的数字串：")
ls = list(map(eval, num.split(',')))
c, h = 50, 30
for d in ls:
    res = round(math.sqrt((2 * c * d) / h))
    print(res, end=',')
print("\b")
