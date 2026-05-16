import itertools
import pandas as pd
import matplotlib.pyplot as plt


def objective(x1, x2, x3):
    return -2 * x1 - 3 * x2 + x3


def is_feasible(x1, x2, x3):
    return (
        2 * x1 + x2 - x3 == -2
        and x1 + 2 * x2 <= 5
        and 3 * x1 - 2 * x2 >= -4
        and x1 >= 0
        and x2 >= 0
        and x3 >= 0
    )


solutions = []

for x1, x2, x3 in itertools.product(range(10), repeat=3):
    if is_feasible(x1, x2, x3):
        z = objective(x1, x2, x3)
        solutions.append([x1, x2, x3, z])

df = pd.DataFrame(solutions, columns=["x1", "x2", "x3", "Z"])

best_value = df["Z"].min()
best_solutions = df[df["Z"] == best_value]

print("Допустимі цілочисельні розв’язки:")
print(df)

print("\nОптимальні цілочисельні розв’язки:")
print(best_solutions)

print(f"\nZmin = {best_value}")

fig, ax = plt.subplots(figsize=(8, 5))
ax.axis("off")

table = ax.table(
    cellText=df.values,
    colLabels=df.columns,
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

plt.title(
    f"Допустимі цілочисельні розв’язки\n"
    f"Zmin = {best_value}",
    pad=20
)

plt.show()