sum = 0
x = 17

for num in range (17,50):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    if sum == 12:
        break
    x+=1

print(x)