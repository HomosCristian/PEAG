import numpy as np

# 5. Scrieți o funcție Python care generează o matrice cu n linii (n parametru de intrare), fiecare linie
# conținând un individ vector binar de dimensiune 8, cu număr impar de biți 1 și calitatea asociată
# șirului. Calitatea unui individ este dată de valoarea în bază 10 a reprezentării binare (individul [0 0 0 0
# 0 0 1 1] are calitatea 3). Calculați și afișați indivizii cei mai buni (cu calitatea maximă).

print("\nExercitiul 5:")


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