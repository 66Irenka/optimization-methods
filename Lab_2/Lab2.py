import numpy as np
import matplotlib.pyplot as plt

# варіант 13
def f(x, y):
    return x**2 + x*y + 3*y**2 - 12*x - 15*y + 2


x = np.linspace(0, 10, 100)
y = np.linspace(-2, 5, 100)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure(figsize=(12, 5))

ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

ax1.set_title('3D поверхня f(x, y)')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('f(x, y)')

ax2 = fig.add_subplot(122)

contours = ax2.contour(X, Y, Z, levels=25)
ax2.clabel(contours, inline=True, fontsize=8)

ax2.plot(5.1818, 1.6364, 'ro', label='Мінімум (5.18, 1.64)')

ax2.set_title('Лінії рівня функції')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()