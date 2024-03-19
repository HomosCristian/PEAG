import numpy as np

# 1. Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓:{(𝑥, 𝑦, 𝑧)⁄𝑥, 𝑦, 𝑧 ∈ [−2,7], 𝑥 + 𝑦 + 𝑧 < 10} → ℝ
# 𝑓(𝑥, 𝑦, 𝑧) = 𝑥^2 - 2y*z
# Generați 20 elemente din spațiul soluțiilor (candidați la soluție), evaluați-le și afișați valorile obținute.

def fmax(x, y, z):
    return x**2 - 2*y*z

# Generarea celor 20 de valori
x_values = np.random.uniform(-2, 7, 20)
y_values = np.random.uniform(-2, 7, 20)
z_values = np.random.uniform(-2, 7, 20)

# Evaluarea functiei
print("Exercitiul 1:")
for i in range(20):
    x = x_values[i]
    y = y_values[i]
    z = z_values[i]
    if x + y + z < 10:
        result = fmax(x, y, z)
        print(f"f({x}, {y}, {z}) = {result}")

# 2. Scrieți o funcție Python care generează o matrice (populație) cu 18 linii vectori cu 6 elemente: 5 biți
# reprezentând un individ și un număr întreg reprezentând calitatea acestuia. Calitatea unui individ este
# dată de numărul perechilor de valori consecutive diferite (de exemplu, calitatea lui [1,0,0,1,1] = 2).
# Calculați și afișați indivizii cu cea mai mare valoare a funcției calitate.

import random

print("\nExercitiul 2:")
def generatePopulation():
    population = []
    for _ in range(18):
        individual = [random.randint(0, 1) for _ in range(5)]  # Generăm 5 biți pentru fiecare individ
        quality = calculateQuality(individual)
        population.append((individual, quality))
    return population

def calculateQuality(individual):
    quality = 0
    for i in range(len(individual) - 1):
        if individual[i] != individual[i + 1]:
            quality += 1
    return quality

def bestInd(population):
    best_individual = max(population, key=lambda x: x[1])  # Selectăm individul cu cea mai mare calitate
    return best_individual

# Generăm populația și afișăm-o
population = generatePopulation()
print("Populație generată:")
for individual, quality in population:
    print(f"Individ: {individual}, Calitate: {quality}")

# Afișăm cel mai bun individ
bestIndividual = bestInd(population)
print("\nCel mai bun individ:")
print(f"Individ: {bestIndividual[0]}, Calitate: {bestIndividual[1]}")


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

# 4. Scieți o funcție Python care generează o matrice cu 15 linii, fiecare linie conținând o permutare de
# dimensiune k (k parametru de intrare) și o valoare care reprezintă calitatea permutării. Calitatea unui
# individ P (permutare de dimensiune k) este dată de numărul perechilor (i,j), i<j, pentru care P(i)-
# P(j)=număr par. Evaluați cei 15 indivizi generați și afișați valoarea maximă.

print("\nExercitiul 4:")

import itertools

def quality_of_permutation(perm):
    """
    Calculează calitatea unei permutări dată de numărul perechilor (i,j), i<j, pentru care P(i) - P(j) este număr par.
    """
    quality = 0
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            if (perm[i] - perm[j]) % 2 == 0:
                quality += 1
    return quality

def generate_population(k, n=15):
    """
    Generează o matrice cu n linii, fiecare linie conținând o permutare de dimensiune k și calitatea permutării.
    """
    population = []
    for _ in range(n):
        perm = np.random.permutation(k)  # Generăm o permutare aleatoare de dimensiune k
        quality = quality_of_permutation(perm)  # Calculăm calitatea permutării
        population.append((perm, quality))
    return population

# Parametrul k pentru dimensiunea permutărilor
k = 5

# Generarea populației de indivizi
population = generate_population(k)

# Afisarea populației și a valorii maxime
print("Populația generată:")
for i, (perm, quality) in enumerate(population, start=1):
    print(f"Individul {i}: Permutare: {perm}, Calitate: {quality}")

max_quality = max([quality for _, quality in population])
print("Valoarea maximă a calității:", max_quality)

# 5. Scrieți o funcție Python care generează o matrice cu n linii (n parametru de intrare), fiecare linie
# conținând un individ vector binar de dimensiune 8, cu număr impar de biți 1 și calitatea asociată
# șirului. Calitatea unui individ este dată de valoarea în bază 10 a reprezentării binare (individul [0 0 0 0
# 0 0 1 1] are calitatea 3). Calculați și afișați indivizii cei mai buni (cu calitatea maximă).

print("\nExercitiul 5:")

import numpy as np

def quality_of_individual(individual):

    return int("".join(str(bit) for bit in individual), 2)

def generate_population(n):

    population = []
    for _ in range(n):
        individual = np.random.randint(0, 2, 8)  # Generăm un individ aleatoriu
        while np.sum(individual) % 2 != 1:  # Verificăm dacă numărul de biți 1 este impar
            individual = np.random.randint(0, 2, 8)
        quality = quality_of_individual(individual)  # Calculăm calitatea individului
        population.append((individual, quality))
    return population

# Parametrul n pentru numărul de indivizi
n = 10

# Generarea populației de indivizi
population = generate_population(n)

# Găsirea indivizilor cu cea mai mare calitate
max_quality = max([quality for _, quality in population])
best_individuals = [individual for individual, quality in population if quality == max_quality]

# Afisarea indivizilor cei mai buni
print("Indivizii cei mai buni:")
for individual in best_individuals:
    print("Individ:", individual, "Calitate:", max_quality)

# 6. Scrieți o funcție Python care generează o matrice cu n linii, fiecare linie conținând o permutare de
# dimensiune 8 (n parametru de intrare) și o valoare care reprezintă calitatea permutării. Calitatea unui
# individ P (permutare de dimensiune 8) este dată de numărul perechilor (i,j), i<j, pentru care P(i)=j și
# P(j)=i. Evaluați cei n indivizi generați și afișați valoarea maximă a calității.

print("\nExercitiul 6:")

def quality_of_permutation(perm):

    quality = 0
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            if perm[i] == j and perm[j] == i:
                quality += 1
    return quality

def generate_population(n):

    population = []
    for _ in range(n):
        perm = np.random.permutation(8)  # Generăm o permutare aleatoare de dimensiune 8
        quality = quality_of_permutation(perm)  # Calculăm calitatea permutării
        population.append((perm, quality))
    return population

# Parametrul n pentru numărul de indivizi
n = 10

# Generarea populației de indivizi
population = generate_population(n)

# Calcularea și afișarea valorii maxime a calității
max_quality = max([quality for _, quality in population])
print("Valoarea maximă a calității:", max_quality)

# 7. Scrieți o funcție Python care generează o matrice cu n linii (n parametru de intrare), fiecare linie
# conținând 9 valori: a) un individ vector de dimensiune 8, cu elemente numere întregi din mulțimea
# {1,2,3,4} și cu proprietatea că în poziția a 5-a valoarea este număr impar; b) calitatea individului.
# Calitatea unui individ este dată de produsul elementelor sale. Calculați și afișați indivizii cei mai slabi
# (cu calitatea minimă).

print("\nExercitiul 7:")

import numpy as np

def quality_of_individual(individual):

    return np.prod(individual)

def generate_population(n):

    population = []
    for _ in range(n):
        individual = np.random.choice([1, 2, 3, 4], size=8)  # Generăm un individ aleatoriu cu elemente din mulțimea {1, 2, 3, 4}
        individual[4] = np.random.choice([1, 3])  # Asigurăm că valoarea din poziția a 5-a este un număr impar
        quality = quality_of_individual(individual)  # Calculăm calitatea individului
        population.append((individual, quality))
    return population

# Parametrul n pentru numărul de indivizi
n = 10

# Generarea populației de indivizi
population = generate_population(n)

# Găsirea indivizilor cei mai slabi (cu calitatea minimă)
min_quality = min([quality for _, quality in population])
worst_individuals = [individual for individual, quality in population if quality == min_quality]

# Afisarea indivizilor cei mai slabi
print("Indivizii cei mai slabi:")
for individual in worst_individuals:
    print("Individ:", individual, "Calitate:", min_quality)

# 8. Scrieți o funcție Python care generează o matrice cu 10 linii, fiecare linie conținând k+1 valori: a) un
# individ vector de dimensiune k, cu elemente numere întregi din mulțimea {−4, −3, −2, −1,1,2,3,4} și
# cu proprietatea că suma elementelor este pozitivă; b) calitatea individului. Calitatea unui individ este
# dată de suma modulelor elementelor sale (de exemplu, pentru k=3 și x=[2,4,-3], x este fezabil, pentru
# că suma elementelor sale este 3>0; calitatea lui x este 9). Calculați și afișați indivizii cei mai slabi (cu
# calitatea minimă).

print("\nExercitiul 8:")

def quality_of_individual(individual):

    return np.sum(np.abs(individual))

def generate_population(k, n):

    population = []
    for _ in range(n):
        individual = np.random.choice([-4, -3, -2, -1, 1, 2, 3, 4], size=k)  # Generăm un individ aleatoriu cu elemente din mulțimea {-4, -3, -2, -1, 1, 2, 3, 4}
        while np.sum(individual) <= 0:  # Verificăm dacă suma elementelor este pozitivă
            individual = np.random.choice([-4, -3, -2, -1, 1, 2, 3, 4], size=k)
        quality = quality_of_individual(individual)  # Calculăm calitatea individului
        population.append((individual, quality))
    return population

# Parametrii k pentru dimensiunea individului și n pentru numărul de indivizi
k = 3
n = 10

# Generarea populației de indivizi
population = generate_population(k, n)

# Găsirea indivizilor cei mai slabi (cu calitatea minimă)
min_quality = min([quality for _, quality in population])
worst_individuals = [individual for individual, quality in population if quality == min_quality]

# Afisarea indivizilor cei mai slabi
print("Indivizii cei mai slabi:")
for individual in worst_individuals:
    print("Individ:", individual, "Calitate:", min_quality)

# 9.  Scrieți o funcție Python care generează o matrice cu 10 linii vectori cu k+1 elemente (k parametru
# dat): k biți reprezentând un individ și un număr întreg reprezentând calitatea acestuia. Calitatea unui
# individ este dată de numărul perechilor de valori consecutive egale. (de exemplu, pentru k=5, calitatea
# lui [0,0,0,1,1] = 3). Afișați indivizii generați în ordinea crescătoare a calităților lor.

print("\nExercitiul 9:")

def quality_of_individual(individual):

    quality = 0
    for i in range(len(individual) - 1):
        if individual[i] == individual[i + 1]:
            quality += 1
    return quality

def generate_population(k, n):

    population = []
    for _ in range(n):
        individual = np.random.randint(0, 2, size=k)  # Generăm un individ aleatoriu de dimensiune k sub forma de biți (0 sau 1)
        quality = quality_of_individual(individual)  # Calculăm calitatea individului
        population.append((individual, quality))
    return population

# Parametrii k pentru dimensiunea individului și n pentru numărul de indivizi
k = 5
n = 10

# Generarea populației de indivizi
population = generate_population(k, n)

# Sortarea populației în funcție de calitatea individului (în ordine crescătoare)
population.sort(key=lambda x: x[1])

# Afisarea indivizilor în ordinea crescătoare a calităților lor
print("Indivizii generați în ordinea crescătoare a calităților:")
for individual, quality in population:
    print("Individ:", individual, "Calitate:", quality)


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


# 14. Scrieți o funcție Python care generează o matrice cu 10 linii, fiecare linie conținând: a) o permutare P
# de dimensiune k (k parametru de intrare), cu proprietatea că P(1)=1 și P(k)=k; b) o valoare care
# reprezintă calitatea permutării. Calitatea unui individ P (permutare de dimensiune k) este dată de
# numărul de elemente i cu proprietatea că P(i)<i. Evaluați cei 10 indivizi generați și afișați valoarea
# maximă.

print("\nExercitiul 14:")


def quality_of_permutation(perm):

    quality = 0
    for i in range(len(perm)):
        if perm[i] < i + 1:
            quality += 1
    return quality

def generate_population(k, n=10):

    population = []
    for _ in range(n):
        perm = np.random.permutation(range(1, k+1))  # Generăm o permutare aleatoare de dimensiune k
        perm[0] = 1  # Asigurăm că P(1) = 1
        perm[-1] = k  # Asigurăm că P(k) = k
        quality = quality_of_permutation(perm)  # Calculăm calitatea permutării
        population.append((perm, quality))
    return population

# Parametrul k pentru dimensiunea permutărilor
k = 5

# Generarea populației de indivizi
population = generate_population(k)

# Afișarea populației și a valorii maxime
print("Populația generată:")
for i, (perm, quality) in enumerate(population, start=1):
    print(f"Individul {i}: Permutare: {perm}, Calitate: {quality}")

max_quality = max([quality for _, quality in population])
print("Valoarea maximă a calității:", max_quality)


# 15. Scrieți o funcție Python care generează o matrice cu n linii (n parametru de intrare), fiecare linie
# conținând 10 elemente: un individ vector binar de dimensiune 9, cu 5 biți egali cu 1 și calitatea asociată
# șirului. Calitatea unui individ este dată de suma pozițiilor care conțin 1. Prima poziție este 0 (de
# exemplu individul [1 0 0 0 1 0 1 1 1] are calitatea 25). Calculați și afișați indivizii generați, împreună cu
# calitățile lor.

print("\nExercitiul 15:")


def quality_of_individual(individual):

    return np.sum(np.where(individual == 1, np.arange(len(individual)), 0))

def generate_population(n):

    population = []
    for _ in range(n):
        individual = np.zeros(9)
        indices = np.random.choice(9, 5, replace=False)  # Generăm 5 indici unici pentru a seta 5 biți la 1
        individual[indices] = 1
        quality = quality_of_individual(individual)  # Calculăm calitatea individului
        population.append((individual, quality))
    return population

# Parametrul n pentru numărul de indivizi în populație
n = 10

# Generarea populației de indivizi
population = generate_population(n)

# Afișarea indivizilor și a calităților lor
print("Indivizii generați:")
for i, (individual, quality) in enumerate(population, start=1):
    print(f"Individul {i}: {individual}, Calitate: {quality}")


# 16. Scrieți o funcție Python care generează o matrice cu n linii, fiecare linie conținând o permutare de
# dimensiune 7 (n parametru de intrare) și o valoare care reprezintă calitatea permutării. Calitatea unui
# individ P (permutare de dimensiune 7) este dată de numărul perechilor (i,i+1), pentru care P(i)=i+1 și
# P(i+1)=i. Evaluați cei n indivizi generați și afișați valoarea maximă a calității.

print("\nExercitiul 16:")

def quality_of_permutation(perm):

    quality = 0
    for i in range(len(perm) - 1):
        if perm[i] == i + 1 and perm[i+1] == i:
            quality += 1
    return quality

def generate_population(n):

    population = []
    for _ in range(n):
        perm = np.random.permutation(7) + 1  # Generăm o permutare aleatoare de dimensiune 7
        quality = quality_of_permutation(perm)  # Calculăm calitatea permutării
        population.append((perm, quality))
    return population

# Parametrul n pentru numărul de indivizi în populație
n = 10

# Generarea populației de indivizi
population = generate_population(n)

# Găsirea și afișarea valorii maxime a calității
max_quality = max([quality for _, quality in population])
print("Valoarea maximă a calității:", max_quality)


# 17. Scrieți o funcție Python care generează o matrice cu 10 linii, fiecare linie conținând k+1 valori (k
# parametru dat): a) un individ vector de dimensiune k, cu elemente numere întregi din mulțimea
# {1,2,3,4,5,6} și cu proprietatea că în ultima poziție valoarea este număr par; b) calitatea individului.
# Calitatea unui individ este dată de produsul elementelor sale. Afișați indivizii generați în ordinea
# crescătoare a calităților.

print("\nExercitiul 17:")

def quality_of_individual(individual):

    return np.prod(individual)

def generate_population(k):

    population = []
    for _ in range(10):
        individual = np.random.randint(1, 7, size=k)  # Generăm un individ aleatoriu cu elemente din mulțimea {1, 2, 3, 4, 5, 6}
        individual[-1] = np.random.choice([2, 4, 6])  # Asigurăm că ultima valoare este un număr par
        quality = quality_of_individual(individual)  # Calculăm calitatea individului
        population.append((individual, quality))
    return population

# Parametrul k pentru dimensiunea individului
k = 5

# Generarea populației de indivizi
population = generate_population(k)

# Sortarea populației în funcție de calitatea individului
population_sorted = sorted(population, key=lambda x: x[1])

# Afișarea indivizilor generați în ordinea crescătoare a calităților
print("Indivizii generați în ordinea crescătoare a calităților:")
for i, (individual, quality) in enumerate(population_sorted, start=1):
    print(f"Individul {i}: {individual}, Calitate: {quality}")


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


# 19. Scrieți o funcție Python care generează o matrice cu n linii (n parametru de intrare), fiecare linie
# conținând: a) o permutare de dimensiune 6 în care valoarea 1 nu apare în prima jumătate; b) o valoare
# care reprezintă calitatea permutării. Calitatea unui individ P (permutare de dimensiune 6) este dată
# de suma pozițiilor pe care apar valorile pare (de exemplu, individul P=[2,5,4,3,0,1] este fezabil pentru
# că 1 apare în ultima poziție; calitatea lui P este 0+2+4=6). Evaluați cei n indivizi generați și afișați
# valoarea maximă a calității.

print("\nExercitiul 19:")

def quality_of_permutation(perm):

    quality = sum(i for i, val in enumerate(perm) if val % 2 == 0)
    return quality

def generate_population(n):

    population = []
    for _ in range(n):
        perm = np.random.permutation(range(6))  # Generăm o permutare aleatoare de dimensiune 6
        # Asigurăm că valoarea 1 nu apare în prima jumătate a permutării
        while 1 in perm[:3]:
            perm = np.random.permutation(range(6))
        quality = quality_of_permutation(perm)  # Calculăm calitatea permutării
        population.append((perm, quality))
    return population

# Parametrul n pentru numărul de indivizi în populație
n = 10

# Generarea populației de indivizi
population = generate_population(n)

# Găsirea și afișarea valorii maxime a calității
max_quality = max([quality for _, quality in population])

print("Valoarea maximă a calității în populație:", max_quality)

# 20. Scrieți o funcție Python care generează o matrice cu 10 linii, fiecare linie conținând 7 valori: a) un
# individ vector de dimensiune 6, cu elemente numere întregi din mulțimea {−2, −1,0,1,2,3,4} și cu
# proprietatea că suma elementelor este mai mică decât 10; b) calitatea individului. Calitatea unui
# individ este dată de produsul valorilor absolute ale elementelor sale. Afișați indivizii generați în
# ordinea inversă a calităților. 

print("\nExercitiul 20:")

def quality_of_individual(individual):

    return np.prod(np.abs(individual))

def generate_population():

    population = []
    for _ in range(10):
        individual = np.random.randint(-2, 5, size=6)  # Generăm un individ aleatoriu cu elemente din mulțimea {-2, -1, 0, 1, 2, 3, 4}
        # Verificăm dacă suma elementelor este mai mică decât 10
        while np.sum(individual) >= 10:
            individual = np.random.randint(-2, 5, size=6)
        quality = quality_of_individual(individual)  # Calculăm calitatea individului
        population.append((individual, quality))
    return population

# Generarea populației de indivizi
population = generate_population()

# Sortarea populației în funcție de calitatea individului în ordine inversă
population_sorted = sorted(population, key=lambda x: x[1], reverse=True)

# Afișarea indivizilor generați în ordinea inversă a calităților
print("Indivizii generați în ordinea inversă a calităților:")
for i, (individual, quality) in enumerate(population_sorted, start=1):
    print(f"Individul {i}: {individual}, Calitate: {quality}")










