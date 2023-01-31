def f(n):
    if n <= 3:
        return n
    if n > 3:
        if n % 2 == 0:
            return 2 * n * n + f(n-1)
        return n * n* n + n + f(n-1)


t = 0
for n in range (1, 1001):
  if f(n) < 10**3:
    t += 1
print(t)