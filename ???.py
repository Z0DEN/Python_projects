ost = ""
result = ""
answ = 0
for x in range (1,100):
    y = 36**17 - 6**x + 71
    while y > 0:
        ost += str(y % 6)
        y //= 6
    ost = ost[(len(ost) - 1):(0):-1]
    for i in ost:
        answ += int(i)
    if answ == 61:
        print(x)
    ost = ''
    answ = 0
        
# def summa(num):
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum
#
# func = summa(y)
# print(y)
# while func > 0:           # реверснутый x в шестиричной системе  (= 16)
#     ost += str(func % 6)
#     func = func // 6
#
# for i in range(1, len(ost)+1):  # нормальный x в шестиричной системе  (= 61)
#     result += ost[-i]
#
# if result == "342":
#     print("x: ", result)
#
# ost = ""
# sum = 0
# # result = ""
# y = 286511795219689093516492871
# while y > 0:
#     ost += str(y%6)
#     y //= 6
# for i in ost[(len(ost)-1):(0):-1]:
#     sum += int(i)
# print(sum)
