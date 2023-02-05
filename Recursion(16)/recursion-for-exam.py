def f(n):
    if n == 1:
        return 1
    if n > 1:
        return (2 * n - 1) * f(n-1)

t = f(16)
y = f(13)
h = t // y
print("", "t = ", t, "\n", "y = ", y, "\n","h = " ,h)