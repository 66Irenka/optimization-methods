import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 180, 500)


y1 = 200 - x        # x + y >= 200
y2 = 300 - 2 * x    # 2x + y <= 300

points = np.array([
    [0, 200],
    [0, 300],
    [100, 100]
])

plt.figure(figsize=(9, 7))

plt.plot(x, y1, label=r'$x + y = 200$')
plt.plot(x, y2, label=r'$2x + y = 300$')

plt.fill(
    points[:, 0],
    points[:, 1],
    alpha=0.3,
    label='Область допустимих розв’язків'
)

for px, py in points:
    plt.scatter(px, py)
    plt.text(px + 3, py + 3, f'({px:.0f}; {py:.0f})')

plt.scatter(0, 200, s=100, label='Оптимальна точка')
plt.text(5, 205, 'Optimum\n(0; 200)', fontsize=10)

z = 600
y_z = (z - 8 * x) / 3
plt.plot(x, y_z, linestyle='--', label=r'$Z_{min}=600$')

plt.xlim(0, 180)
plt.ylim(0, 330)

plt.xlabel('x — журнали на швидкому сховищі')
plt.ylabel('y — журнали на архівному сховищі')
plt.title('Графічне розв’язання задачі лінійного програмування')

plt.grid(True)
plt.legend()
plt.show()