import numpy as np

# 10. Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓:{𝑥 = (𝑥1, … , 𝑥10)⁄𝑥𝑖 ∈ {−1,1}, 𝑥1 + ⋯ + 𝑥9 + 𝑥10 ≥ 0} → ℝ
# 𝑓(𝑥) = 𝑎 ∙ 𝑥1 + ⋯ + 𝑎 ∙ 𝑥10
# unde 𝑎 este un parametru dat.
# Generați o populație cu n elemente (n parametru dat), evaluați-le și afișați calitatea maximă.

print("\nExercitiul 10:")

def f(x, a):

    return np.dot(a, x)

def generate_population(n):

    population = []
    for _ in range(n):
        individual = np.random.choice([-1, 1], size=10)  # Generăm un individ aleatoriu cu valori -1 sau 1
        population.append(individual)
    return population

# Parametrii a și n pentru funcția de maxim și numărul de indivizi din populație
a = np.random.rand(10)  # Generăm un vector a aleatoriu
n = 100

# Generarea populației de indivizi
population = generate_population(n)

# Evaluarea calității fiecărui individ și găsirea calității maxime
max_quality = float('-inf')
for individual in population:
    quality = f(individual, a)
    if quality > max_quality:
        max_quality = quality

print("Calitatea maximă în populație:", max_quality)