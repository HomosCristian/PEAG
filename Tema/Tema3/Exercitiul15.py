import numpy as np

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
