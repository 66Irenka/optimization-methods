import math
import matplotlib.pyplot as plt

# варіант 13
def f(x):
    return x - 2 * math.sqrt(x)


a = 0.5
b = 2
eps = 1e-4


def dichotomy_min(a, b, eps):
    delta = eps / 2
    iterations = 0

    while (b - a) > eps:
        x1 = (a + b - delta) / 2
        x2 = (a + b + delta) / 2

        if f(x1) < f(x2):
            b = x2
        else:
            a = x1

        iterations += 1

    x_opt = (a + b) / 2
    return x_opt, f(x_opt), iterations


def golden_section_min(a, b, eps):
    phi = (1 + math.sqrt(5)) / 2
    iterations = 0

    x1 = b - (b - a) / phi
    x2 = a + (b - a) / phi

    while (b - a) > eps:
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = b - (b - a) / phi
        else:
            a = x1
            x1 = x2
            x2 = a + (b - a) / phi

        iterations += 1

    x_opt = (a + b) / 2
    return x_opt, f(x_opt), iterations


def fibonacci_min(a, b, eps):
    fib = [1, 1]

    while fib[-1] < (b - a) / eps:
        fib.append(fib[-1] + fib[-2])

    n = len(fib) - 1
    iterations = 0

    x1 = a + fib[n - 2] / fib[n] * (b - a)
    x2 = a + fib[n - 1] / fib[n] * (b - a)

    for k in range(1, n - 1):
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + fib[n - k - 2] / fib[n - k] * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + fib[n - k - 1] / fib[n - k] * (b - a)

        iterations += 1

    x_opt = (a + b) / 2
    return x_opt, f(x_opt), iterations


dichotomy_result = dichotomy_min(a, b, eps)
golden_result = golden_section_min(a, b, eps)
fibonacci_result = fibonacci_min(a, b, eps)

columns = [
    "Дихотомії",
    "Золотого перетину",
    "Фібоначчі"
]

rows = [
    "К-ть ітерацій",
    "x*",
    "f(x*)"
]

table_data = [
    [
        dichotomy_result[2],
        golden_result[2],
        fibonacci_result[2]
    ],
    [
        f"{dichotomy_result[0]:.4f}",
        f"{golden_result[0]:.4f}",
        f"{fibonacci_result[0]:.4f}"
    ],
    [
        f"{dichotomy_result[1]:.4f}",
        f"{golden_result[1]:.4f}",
        f"{fibonacci_result[1]:.4f}"
    ]
]

fig, ax = plt.subplots(figsize=(10, 3))

ax.axis('off')

table = ax.table(
    cellText=table_data,
    rowLabels=rows,
    colLabels=columns,
    loc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2.5)

plt.title("Порівняння ефективності методів", pad=12)

plt.show()