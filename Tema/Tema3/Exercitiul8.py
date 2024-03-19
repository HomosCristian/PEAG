import numpy as np

# 8. Scrieți o funcție Python care generează o matrice cu 10 linii, fiecare linie conținând k+1 valori: a) un
# individ vector de dimensiune k, cu elemente numere întregi din mulțimea {−4, −3, −2, −1,1,2,3,4} și
# cu proprietatea că suma elementelor este pozitivă; b) calitatea individului. Calitatea unui individ este
# dată de suma modulelor elementelor sale (de exemplu, pentru k=3 și x=[2,4,-3], x este fezabil, pentru
# că suma elementelor sale este 3>0; calitatea lui x este 9). Calculați și afișați indivizii cei mai slabi (cu
# calitatea minimă).

print("\nExercitiul 8:")

def quality_of_individual(individual):

    return np.sum(np.abs(individual))

def generate_population(k, n):

    population = []
    for _ in range(n):
        individual = np.random.choice([-4, -3, -2, -1, 1, 2, 3, 4], size=k)  # Generăm un individ aleatoriu cu elemente din mulțimea {-4, -3, -2, -1, 1, 2, 3, 4}
        while np.sum(individual) <= 0:  # Verificăm dacă suma elementelor este pozitivă
            individual = np.random.choice([-4, -3, -2, -1, 1, 2, 3, 4], size=k)
        quality = quality_of_individual(individual)  # Calculăm calitatea individului
        population.append((individual, quality))
    return population

# Parametrii k pentru dimensiunea individului și n pentru numărul de indivizi
k = 3
n = 10

# Generarea populației de indivizi
population = generate_population(k, n)

# Găsirea indivizilor cei mai slabi (cu calitatea minimă)
min_quality = min([quality for _, quality in population])
worst_individuals = [individual for individual, quality in population if quality == min_quality]

# Afisarea indivizilor cei mai slabi
print("Indivizii cei mai slabi:")
for individual in worst_individuals:
    print("Individ:", individual, "Calitate:", min_quality)