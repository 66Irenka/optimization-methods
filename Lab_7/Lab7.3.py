import numpy as np

def f(x):
    x1, x2, x3 = x
    return x1**2 - x1*x2 + 2*x2**2 + x2*x3 + 2*x3**2 - 15


def grad_f(x):
    x1, x2, x3 = x

    return np.array([
        2*x1 - x2,
        -x1 + 4*x2 + x3,
        x2 + 4*x3
    ])


x = np.array([1.0, 1.0, 1.0])

alpha = 0.05
eps = 1e-4
max_iter = 10000
iterations = 0

while np.linalg.norm(grad_f(x)) > eps and iterations < max_iter:
    x = x - alpha * grad_f(x)
    iterations += 1

print("Мінімум без урахування обмежень методом градієнтного спуску")
print(f"x1* = {x[0]:.4f}")
print(f"x2* = {x[1]:.4f}")
print(f"x3* = {x[2]:.4f}")
print(f"fmin = {f(x):.4f}")
print(f"Кількість ітерацій = {iterations}")