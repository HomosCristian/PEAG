import numpy as np

# 3. Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓:{𝑥 = (𝑥1, … , 𝑥10)⁄𝑥𝑖 ∈ [−1,1], 𝑥1 + ⋯ + 𝑥9 = 1 − 𝑥10} → ℝ
# 𝑓(𝑥) = 𝑎1 ∙ 𝑥1 + ⋯ + 𝑎10 ∙ 𝑥10
# unde 𝑎 = (𝑎1, … , 𝑎10) este un vector constant, dată de intrare.
# Generați 10 elemente din spațiul soluțiilor, evaluați-le și afișați valorea medie obținută.

print("\nExercitiul 3:")

def f(x, a):

    return np.dot(a, x)

# Definirea vectorului constant a
a = np.random.rand(10)

# Generarea a 10 elemente din spațiul soluțiilor
solutions = []
for _ in range(10):
    x = np.random.uniform(-1, 1, 10)  # Generăm un vector x cu valori între -1 și 1
    x[9] = 1 - np.sum(x[:9])  # Garantăm că suma primelor 9 componente este 1 - x10
    solutions.append(x)

# Evaluarea și afișarea valorii medii obținute
mean_value = np.mean([f(x, a) for x in solutions])
print("Valoarea medie obținută:", mean_value)