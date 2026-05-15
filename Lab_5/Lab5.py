import numpy as np
import matplotlib.pyplot as plt

# Варіант 13
columns = ["x", "y", "s1", "a1", "s2", "b"]

tableau = np.array([
    [1, 1, -1, 1, 0, 200],
    [2, 1,  0, 0, 1, 300],
    [0, -1, 1, 0, 0, -200]
], dtype=float)

basis = ["a1", "s2"]
tableaus = []


def save_tableau(tableau, basis, title):
    data = []

    for i in range(len(basis)):
        row = [basis[i]] + [f"{value:.4f}" for value in tableau[i]]
        data.append(row)

    z_row = ["W"] + [f"{value:.4f}" for value in tableau[-1]]
    data.append(z_row)

    tableaus.append((title, data))


save_tableau(tableau.copy(), basis.copy(), "Початкова симплекс-таблиця")


pivot_col = 1

ratios = []
for i in range(2):
    if tableau[i, pivot_col] > 0:
        ratios.append(tableau[i, -1] / tableau[i, pivot_col])
    else:
        ratios.append(np.inf)

pivot_row = np.argmin(ratios)
basis[pivot_row] = columns[pivot_col]

pivot = tableau[pivot_row, pivot_col]
tableau[pivot_row] = tableau[pivot_row] / pivot

for i in range(3):
    if i != pivot_row:
        tableau[i] = tableau[i] - tableau[i, pivot_col] * tableau[pivot_row]

save_tableau(tableau.copy(), basis.copy(), "Симплекс-таблиця після Фази I")


x_opt = 0
y_opt = 200
z_min = 8 * x_opt + 3 * y_opt

print("Оптимальний розв’язок:")
print(f"x* = {x_opt:.4f}")
print(f"y* = {y_opt:.4f}")
print(f"Zmin = {z_min:.4f}")

for idx, (title, tab) in enumerate(tableaus):
    fig, ax = plt.subplots(figsize=(10, 3))
    ax.axis("off")

    table = ax.table(
        cellText=tab,
        colLabels=["Базис"] + columns,
        loc="center"
    )

    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 2)

    plt.title(title)
    plt.show()

x = np.linspace(0, 180, 500)

y1 = 200 - x
y2 = 300 - 2 * x

points = np.array([
    [0, 200],
    [0, 300],
    [100, 100]
])

plt.figure(figsize=(9, 7))

plt.plot(x, y1, label=r"$x + y = 200$")
plt.plot(x, y2, label=r"$2x + y = 300$")

plt.fill(
    points[:, 0],
    points[:, 1],
    alpha=0.3,
    label="Область допустимих розв’язків"
)

for px, py in points:
    plt.scatter(px, py)
    plt.text(px + 3, py + 3, f"({px:.0f}; {py:.0f})")

plt.scatter(x_opt, y_opt, s=120, label="Оптимальна точка")
plt.text(x_opt + 5, y_opt + 5, f"Optimum\n({x_opt}; {y_opt})")

y_z = (z_min - 8 * x) / 3
plt.plot(x, y_z, linestyle="--", label=rf"$Z_{{min}}={z_min}$")

plt.xlim(0, 180)
plt.ylim(0, 330)

plt.xlabel("x — журнали на швидкому сховищі")
plt.ylabel("y — журнали на архівному сховищі")
plt.title("Розв’язання задачі симплекс-методом")

plt.grid(True)
plt.legend()
plt.show()