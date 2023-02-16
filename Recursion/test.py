count = 0
flag = 0
k = 0
for n in range(1,100):
    flag = 0
    k = 0
    while n > 0:
            flag += 1
            if n % 10 % 2 != 0:
                break
            else:
                n //= 10
                k += 1
    if flag == k:
        count += 1
print("count -",count)
