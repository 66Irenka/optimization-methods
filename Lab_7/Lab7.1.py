import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

t = sp.symbols("t")

x1_t = t - 3
x2_t = 11 + 2 * t
x3_t = t

f_t = x1_t**2 - x1_t * x2_t + 2 * x2_t**2 + x2_t * x3_t + 2 * x3_t**2 - 15
f_t = sp.expand(f_t)

df_t = sp.diff(f_t, t)
t_opt = sp.solve(sp.Eq(df_t, 0), t)[0]

x1_opt = x1_t.subs(t, t_opt)
x2_opt = x2_t.subs(t, t_opt)
x3_opt = x3_t.subs(t, t_opt)
f_min = f_t.subs(t, t_opt)

print("Графічний метод")
print(f"f(t) = {f_t}")
print(f"t* = {float(t_opt):.4f}")
print(f"x1* = {float(x1_opt):.4f}")
print(f"x2* = {float(x2_opt):.4f}")
print(f"x3* = {float(x3_opt):.4f}")
print(f"fmin = {float(f_min):.4f}")

f_lambdified = sp.lambdify(t, f_t, "numpy")

t_values = np.linspace(-10, 3, 500)
f_values = f_lambdified(t_values)

plt.figure(figsize=(9, 6))
plt.plot(t_values, f_values, label=f"f(t) = {f_t}")
plt.scatter(float(t_opt), float(f_min), s=100, label="Точка мінімуму")

plt.text(
    float(t_opt) + 0.3,
    float(f_min) + 20,
    f"t* = {float(t_opt):.4f}\nfmin = {float(f_min):.4f}",
    fontsize=10
)

plt.title("Графічне знаходження мінімуму функції")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.grid(True)
plt.legend()
plt.show()
