def convert_number_system(number, base):
    residue = ""
    while number > 0:  # реверснутый  в шестиричной системе
        residue += str(number % base)
        number = number // base

    result = ""
    for i in range(1, len(residue) + 1):  # нормальный x в шестиричной системе  (= 61)
        result += residue[-i]
    return int(result)


def summa(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


ost = ""
result = ""

for x in range(1, 30):
    y = 36**17 - 6**x + 71

    result = convert_number_system(y, 6)
    sum_func_result = summa(result)

    if sum_func_result == 61:
        print("x: ", x)
