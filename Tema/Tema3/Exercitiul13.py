import numpy as np

# 13. Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓:{𝑥 = (𝑥1, … , 𝑥7)⁄𝑥𝑖 ∈ [−10,10], 𝑥1 + ⋯ + 𝑥7 ≤ 10} → ℝ
# 𝑓(𝑥) = 𝑎1 ∙ 𝑥1 + ⋯ + 𝑎7 ∙ 𝑥7
# unde 𝑎 = (𝑎1, … , 𝑎7) este un vector constant, dată de intrare.
# Generați 10 elemente din spațiul soluțiilor, evaluați-le și afișați calitatea maximă și un individ cu acea
# calitate.

print("\nExercitiul 13:")


def f(x, a):

    return np.dot(a, x)

def generate_solutions(n):

    solutions = []
    for _ in range(n):
        x = np.random.uniform(-10, 10, 7)  # Generăm un vector x cu valori între -10 și 10
        while np.sum(x) > 10:  # Verificăm dacă suma elementelor este mai mică sau egală cu 10
            x = np.random.uniform(-10, 10, 7)
        solutions.append(x)
    return solutions

# Parametrul n pentru numărul de elemente din spațiul soluțiilor
n = 10

# Definirea vectorului constant a
a = np.random.rand(7)

# Generarea a 10 elemente din spațiul soluțiilor
solutions = generate_solutions(n)

# Evaluarea fiecărui element și găsirea celui cu cea mai mare calitate
max_quality = float('-inf')
best_solution = None
for solution in solutions:
    quality = f(solution, a)
    if quality > max_quality:
        max_quality = quality
        best_solution = solution

print("Calitatea maximă:", max_quality)
print("Un individ cu această calitate:", best_solution)