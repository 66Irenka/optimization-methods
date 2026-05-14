import numpy as np
import matplotlib.pyplot as plt

# варіант 13
def f(x):
    return x - 2 * np.sqrt(x)


def df(x):
    return 1 - 1 / np.sqrt(x)


a = 0.5
b = 2

x = np.linspace(a, b, 500)

x_min = 1
y_min = f(x_min)

plt.figure(figsize=(10, 5))

plt.plot(x, f(x), label='f(x) = x - 2√x', linewidth=2)
plt.plot(x, df(x), label="f'(x)", linewidth=2)

plt.scatter(
    x_min,
    y_min,
    color='red',
    s=80,
    label=f'Min ({x_min:.4f}, {y_min:.4f})'
)

plt.title('Графік функції та її першої похідної')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.show()

print(f"Точка мінімуму x* = {x_min:.4f}")
print(f"Значення функції f(x*) = {y_min:.4f}")
