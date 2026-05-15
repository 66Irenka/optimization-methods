import numpy as np
import matplotlib.pyplot as plt

costs = np.array([
    [3, 2, 4, 1],
    [2, 3, 1, 5],
    [3, 2, 7, 4]
], dtype=float)

supply = np.array([50, 40, 20], dtype=float)

demand = np.array([30, 25, 35, 20], dtype=float)

plan = np.array([
    [5, 25, 0, 20],
    [5, 0, 35, 0],
    [20, 0, 0, 0]
], dtype=float)

total_cost = np.sum(plan * costs)

print("Оптимальний план перевезень:")
print(plan)

print(f"\nZmin = {total_cost:.4f}")


row_labels = [f"A{i+1}" for i in range(len(supply))]
col_labels = [f"B{j+1}" for j in range(len(demand))]

table_data = []

for i in range(len(supply)):
    row = []

    for j in range(len(demand)):
        row.append(
            f"x={plan[i, j]:.0f}\n"
            f"c={costs[i, j]:.0f}"
        )

    table_data.append(row)

fig, ax = plt.subplots(figsize=(10, 4))

ax.axis("off")

table = ax.table(
    cellText=table_data,
    rowLabels=row_labels,
    colLabels=col_labels,
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2.5)

plt.title(
    "Оптимальний план перевезень методом потенціалів\n"
    f"Zmin = {total_cost:.4f}"
)

plt.figtext(
    0.02,
    0.02,
    "Позначення:\n"
    "x = обсяг перевезення\n"
    "c = тариф перевезення",
    fontsize=10,
    ha="left"
)

plt.show()
