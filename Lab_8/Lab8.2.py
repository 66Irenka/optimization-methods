import matplotlib.pyplot as plt

# Варіант 13
x1_relaxed = 0.25
x2_relaxed = 2.375
x3_relaxed = 2 * x1_relaxed + x2_relaxed + 2
z_relaxed = -2 * x1_relaxed - 3 * x2_relaxed + x3_relaxed

integer_solutions = []

for x1 in range(10):
    for x2 in range(10):
        x3 = 2 * x1 + x2 + 2

        if (
            x1 + 2 * x2 <= 5
            and 3 * x1 - 2 * x2 >= -4
            and x1 >= 0
            and x2 >= 0
            and x3 >= 0
            and x2 <= 2
        ):
            z = -2 * x1 - 3 * x2 + x3
            integer_solutions.append([x1, x2, x3, z])

best_value = min(row[3] for row in integer_solutions)
best_solutions = [row for row in integer_solutions if row[3] == best_value]

print("Розв’язок без умови цілочисельності:")
print(f"x1 = {x1_relaxed:.4f}")
print(f"x2 = {x2_relaxed:.4f}")
print(f"x3 = {x3_relaxed:.4f}")
print(f"Z = {z_relaxed:.4f}")

print("\nПісля додавання відсікання Гоморі:")
for row in best_solutions:
    print(f"x1* = {row[0]}")
    print(f"x2* = {row[1]}")
    print(f"x3* = {row[2]}")
    print(f"Zmin = {row[3]}")
    print("---")

table_data = [
    ["Без цілочисельності", f"{x1_relaxed:.4f}", f"{x2_relaxed:.4f}", f"{x3_relaxed:.4f}", f"{z_relaxed:.4f}"]
]

for row in best_solutions:
    table_data.append(["Метод Гоморі", row[0], row[1], row[2], row[3]])

columns = ["Метод", "x1", "x2", "x3", "Z"]

fig, ax = plt.subplots(figsize=(9, 3))
ax.axis("off")

table = ax.table(
    cellText=table_data,
    colLabels=columns,
    loc="center"
)

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 2.5)

plt.title("Результати розв’язання методом Гоморі", pad=1)
plt.show()