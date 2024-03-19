import numpy as np

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