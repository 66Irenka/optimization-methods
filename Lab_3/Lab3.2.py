import numpy as np

# Функція з варіанту 13
def f(x, y):
    return x**2 + x*y + 3*y**2 - 12*x - 15*y + 2

def grad_f(point):
    x, y = point

    return np.array([
        2*x + y - 12,
        x + 6*y - 15
    ])

def hessian_f():
    return np.array([
        [2, 1],
        [1, 6]
    ])

def marquardt_method(x0, eps=1e-4, mu=0.01, max_iter=1000):
    x = np.array(x0, dtype=float)
    iters = 0

    for _ in range(max_iter):
        grad = grad_f(x)

        if np.linalg.norm(grad) < eps:
            break

        H = hessian_f()
        I = np.eye(len(x))

        direction = -np.linalg.inv(H + mu * I) @ grad

        x_new = x + direction

        if f(x_new[0], x_new[1]) < f(x[0], x[1]):
            x = x_new
            mu = mu / 2
        else:
            mu = mu * 2

        iters += 1

    return x, f(x[0], x[1]), iters


if __name__ == "__main__":
    start_point = [0.0, 0.0]

    point, value, iters = marquardt_method(start_point)

    print("Метод Марквардта")
    print("-" * 45)
    print(f"Кількість ітерацій: {iters}")
    print(f"x* = {point[0]:.4f}")
    print(f"y* = {point[1]:.4f}")
    print(f"f(x*, y*) = {value:.4f}")