import numpy as np

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
