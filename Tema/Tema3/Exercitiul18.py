import numpy as np

# 18. Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓:{𝑥 = (𝑥1, … , 𝑥8/𝑥𝑖 ∈ {−1,1}, 𝑥1 + 𝑥2 + 𝑥3 + 𝑥4 ≥ 𝑥5 + 𝑥6 + 𝑥7 + 𝑥8} → ℝ
# 𝑓(𝑥) = 𝑥1 + 𝑥2 + 𝑥3 + 𝑥4 − (𝑥5 + 𝑥6 + 𝑥7 + 𝑥8)
# Generați n elemente din spațiul soluțiilor (n parametru dat), evaluați-le și afișați calitatea maximă.

print("\nExercitiul 18:")

def f(x):

    return x[0] + x[1] + x[2] + x[3] - (x[4] + x[5] + x[6] + x[7])

def generate_solutions(n):

    solutions = []
    for _ in range(n):
        # Generăm un vector aleatoriu cu valori -1 sau 1
        x = np.random.choice([-1, 1], size=8)
        # Verificăm dacă condiția specificată este îndeplinită
        if np.sum(x[:4]) >= np.sum(x[4:]):
            solutions.append(x)
    return solutions

# Parametrul n pentru numărul de elemente din spațiul soluțiilor
n = 10

# Generarea a n elemente din spațiul soluțiilor
solutions = generate_solutions(n)

# Evaluarea fiecărui element și găsirea celui cu cea mai mare calitate
max_quality = max([f(x) for x in solutions])

print("Calitatea maximă în spațiul soluțiilor:", max_quality)