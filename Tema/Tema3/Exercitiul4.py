import numpy as np

# 4. Scieți o funcție Python care generează o matrice cu 15 linii, fiecare linie conținând o permutare de
# dimensiune k (k parametru de intrare) și o valoare care reprezintă calitatea permutării. Calitatea unui
# individ P (permutare de dimensiune k) este dată de numărul perechilor (i,j), i<j, pentru care P(i)-
# P(j)=număr par. Evaluați cei 15 indivizi generați și afișați valoarea maximă.

print("\nExercitiul 4:")

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