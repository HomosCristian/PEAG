import numpy as np

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