import sympy as sp

x1, x2, x3 = sp.symbols("x1 x2 x3")
l1, l2 = sp.symbols("l1 l2")

f = x1**2 - x1*x2 + 2*x2**2 + x2*x3 + 2*x3**2 - 15

g1 = x1 - x3 + 3
g2 = 2*x1 + x2 - 4*x3 - 5

L = f + l1 * g1 + l2 * g2

eq1 = sp.diff(L, x1)
eq2 = sp.diff(L, x2)
eq3 = sp.diff(L, x3)
eq4 = sp.diff(L, l1)
eq5 = sp.diff(L, l2)

solution = sp.solve(
    [eq1, eq2, eq3, eq4, eq5],
    [x1, x2, x3, l1, l2],
    dict=True
)

sol = solution[0]

x1_opt = sol[x1]
x2_opt = sol[x2]
x3_opt = sol[x3]

f_min = f.subs({
    x1: x1_opt,
    x2: x2_opt,
    x3: x3_opt
})

print("Метод множників Лагранжа")
print(f"x1* = {float(x1_opt):.4f}")
print(f"x2* = {float(x2_opt):.4f}")
print(f"x3* = {float(x3_opt):.4f}")
print(f"lambda1 = {float(sol[l1]):.4f}")
print(f"lambda2 = {float(sol[l2]):.4f}")
print(f"fmin = {float(f_min):.4f}")