import numpy as np

# варіант 13
def f(x, y):
    return x**2 + x*y + 3*y**2 - 12*x - 15*y + 2


def grad_f(point):
    x, y = point

    return np.array([
        2*x + y - 12,
        x + 6*y - 15
    ])


A = np.array([
    [2, 1],
    [1, 6]
])

def gradient_descent(x0, lr=0.08, eps=1e-4, max_iter=1000):

    p = np.array(x0, dtype=float)
    iters = 0

    for _ in range(max_iter):

        g = grad_f(p)

        if np.linalg.norm(g) < eps:
            break

        p = p - lr * g
        iters += 1

    return p, f(p[0], p[1]), iters


def steepest_descent(x0, eps=1e-4, max_iter=1000):

    p = np.array(x0, dtype=float)
    iters = 0

    for _ in range(max_iter):

        g = grad_f(p)

        if np.linalg.norm(g) < eps:
            break

        alpha = np.dot(g, g) / np.dot(g, A @ g)

        p = p - alpha * g
        iters += 1

    return p, f(p[0], p[1]), iters


def fletcher_reeves(x0, eps=1e-4, max_iter=1000):

    p = np.array(x0, dtype=float)

    g = grad_f(p)
    d = -g

    iters = 0

    for _ in range(max_iter):

        if np.linalg.norm(g) < eps:
            break

        alpha = -np.dot(g, d) / np.dot(d, A @ d)

        p_new = p + alpha * d
        g_new = grad_f(p_new)

        beta = np.dot(g_new, g_new) / np.dot(g, g)

        d = -g_new + beta * d

        p = p_new
        g = g_new

        iters += 1

    return p, f(p[0], p[1]), iters


if __name__ == "__main__":

    start_point = [0.0, 0.0]

    res_gd = gradient_descent(start_point)
    res_sd = steepest_descent(start_point)
    res_fr = fletcher_reeves(start_point)

    methods = [
        ("Градієнтний спуск", res_gd[0], res_gd[1], res_gd[2]),
        ("Найшвидший спуск", res_sd[0], res_sd[1], res_sd[2]),
        ("Флетчера-Рівса", res_fr[0], res_fr[1], res_fr[2])
    ]

    print(f"\n{'Метод':<25} | {'Ітерації':<10} | {'x*':<10} | {'y*':<10} | {'f(x*, y*)':<12}")

    print("-" * 85)

    for name, point, val, iters in methods:

        print(
            f"{name:<25} | "
            f"{iters:<10} | "
            f"{point[0]:<10.4f} | "
            f"{point[1]:<10.4f} | "
            f"{val:<12.4f}"
        )