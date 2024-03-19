import numpy as np

# 11. Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓:{(𝑥, 𝑦, 𝑧,𝑡)⁄𝑥, 𝑦, 𝑧,𝑡 ∈ [−2,2],𝑡 = 𝑥 + 𝑦 − 𝑧} → ℝ
# 𝑓(𝑥, 𝑦, 𝑧) = 𝑡 ∙ 𝑥
# 2 − 2𝑦 ∙ 𝑧
# Generați n elemente din spațiul soluțiilor (n parametru dat), evaluați-le și afișați calitatea maximă.

print("\nExercitiul 11:")

def f(x, y, z):

    t = x + y - z
    return t * x**2 - 2 * y * z

def generate_solutions(n):

    solutions = []
    for _ in range(n):
        x = np.random.uniform(-2, 2)
        y = np.random.uniform(-2, 2)
        z = np.random.uniform(-2, 2)
        t = x + y - z
        solutions.append((x, y, z, t))
    return solutions

# Parametrul n pentru numărul de elemente din spațiul soluțiilor
n = 10

# Generarea elementelor din spațiul soluțiilor
solutions = generate_solutions(n)

# Evaluarea și afișarea calității maxime
max_quality = float('-inf')
for x, y, z, _ in solutions:
    quality = f(x, y, z)
    if quality > max_quality:
        max_quality = quality

print("Calitatea maximă:", max_quality)