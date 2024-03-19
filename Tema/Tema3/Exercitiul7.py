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