x = 0
A = 0

for A in range(1,1000):
    fl = True
    for x in range(1,1000):
        if not ((x // 2) <= (not (x // 3)) or (x + A >= 80)):
            fl = False
            break
    if fl == False:
        break
if fl:
    print(x, A)
