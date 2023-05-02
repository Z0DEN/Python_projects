import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Установка параметров графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Определение функции для создания поверхности
def f(x, y):
    return x**2 - y**2

# Определение диапазона значений x и y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Вычисление значений функции z
Z = f(X, Y)

# Отрисовка поверхности
surf = ax.plot_surface(X, Y, Z, cmap='plasma', alpha=0.8)

# Установка начального угла обзора
ax.view_init(elev=20, azim=30)

# Создание анимации
def animate(i):
    ax.view_init(elev=20, azim=i)
    return None,

# Запуск анимации
ani = animation.FuncAnimation(fig, animate, frames=360, interval=50, blit=True)

plt.show()