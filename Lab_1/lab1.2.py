import numpy as np
import matplotlib.pyplot as plt

# варіант 13
def f(x, y):
    return x**2 + x*y + 3*y**2 - 12*x - 15*y + 2


x = np.linspace(-2, 10, 200)
y = np.linspace(-2, 8, 200)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(10, 7))

ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z, cmap='viridis')

ax.set_title('Графік функції f(x, y)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

plt.show()

plt.figure(figsize=(8, 6))

contour = plt.contour(X, Y, Z, levels=25)

plt.clabel(contour, inline=True, fontsize=8)

plt.title('Лінії рівня функції f(x, y)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

plt.show()