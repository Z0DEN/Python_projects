k = 0
for a in range(1,21):
    while a > 0:
        if ((a % 10) % 2) != 0:
            break
        a //= 10
        k += 1

print(k)