import numpy as np

# 19. Scrieți o funcție Python care generează o matrice cu n linii (n parametru de intrare), fiecare linie
# conținând: a) o permutare de dimensiune 6 în care valoarea 1 nu apare în prima jumătate; b) o valoare
# care reprezintă calitatea permutării. Calitatea unui individ P (permutare de dimensiune 6) este dată
# de suma pozițiilor pe care apar valorile pare (de exemplu, individul P=[2,5,4,3,0,1] este fezabil pentru
# că 1 apare în ultima poziție; calitatea lui P este 0+2+4=6). Evaluați cei n indivizi generați și afișați
# valoarea maximă a calității.

print("\nExercitiul 19:")

def quality_of_permutation(perm):

    quality = sum(i for i, val in enumerate(perm) if val % 2 == 0)
    return quality

def generate_population(n):

    population = []
    for _ in range(n):
        perm = np.random.permutation(range(6))  # Generăm o permutare aleatoare de dimensiune 6
        # Asigurăm că valoarea 1 nu apare în prima jumătate a permutării
        while 1 in perm[:3]:
            perm = np.random.permutation(range(6))
        quality = quality_of_permutation(perm)  # Calculăm calitatea permutării
        population.append((perm, quality))
    return population

# Parametrul n pentru numărul de indivizi în populație
n = 10

# Generarea populației de indivizi
population = generate_population(n)

# Găsirea și afișarea valorii maxime a calității
max_quality = max([quality for _, quality in population])

print("Valoarea maximă a calității în populație:", max_quality)
