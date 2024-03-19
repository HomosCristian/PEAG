import numpy as np

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