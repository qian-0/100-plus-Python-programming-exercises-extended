
# num = int(input("请输入一个数字："))
# res = 1
# for i in range(2, num + 1):
#     res *= i
# print(res)

str_ = input("请输入一串数字（以逗号为间隔）：")
ls = list(map(eval, str_.split(',')))
for i in ls:
    res = 1
    for j in range(2, i+1):
        res *= j
    print(res, end=',')
print("\b")

