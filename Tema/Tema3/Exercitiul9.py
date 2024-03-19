import numpy as np

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