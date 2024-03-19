import numpy as np

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