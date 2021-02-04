# ls = []
# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         ls.append(i)
#         ls.append(",")
# for j in ls[0:-1]:
#     print(j, end="")


# ls = []
# for i in range(2000, 3201):
#     if (i % 7 == 0) and (i % 5 != 0):
#         ls.append(str(i))
# str_ = ','.join(ls)
# print(str_)


for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')
print("\b")     # 表示退格，\n表换行，\r表回车
