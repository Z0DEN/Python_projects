def convert_number_system(number, base):
    residue = ""
    while number > 0:  # реверснутый  в шестиричной системе
        residue += str(number % base)
        number = number // base

    result = ""
    for i in range(1, len(residue) + 1):  # нормальный x в шестиричной системе  (= 61)
        result += residue[-i]
    return int(result)
