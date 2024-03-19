import random

# 2. Scrieți o funcție Python care generează o matrice (populație) cu 18 linii vectori cu 6 elemente: 5 biți
# reprezentând un individ și un număr întreg reprezentând calitatea acestuia. Calitatea unui individ este
# dată de numărul perechilor de valori consecutive diferite (de exemplu, calitatea lui [1,0,0,1,1] = 2).
# Calculați și afișați indivizii cu cea mai mare valoare a funcției calitate.

print("\nExercitiul 2:")
def generatePopulation():
    population = []
    for _ in range(18):
        individual = [random.randint(0, 1) for _ in range(5)]  # Generăm 5 biți pentru fiecare individ
        quality = calculateQuality(individual)
        population.append((individual, quality))
    return population

def calculateQuality(individual):
    quality = 0
    for i in range(len(individual) - 1):
        if individual[i] != individual[i + 1]:
            quality += 1
    return quality

def bestInd(population):
    best_individual = max(population, key=lambda x: x[1])  # Selectăm individul cu cea mai mare calitate
    return best_individual

# Generăm populația și afișăm-o
population = generatePopulation()
print("Populație generată:")
for individual, quality in population:
    print(f"Individ: {individual}, Calitate: {quality}")

# Afișăm cel mai bun individ
bestIndividual = bestInd(population)
print("\nCel mai bun individ:")
print(f"Individ: {bestIndividual[0]}, Calitate: {bestIndividual[1]}")