# 1. Calculați numărul liniilor unei matrice cu proprietatea că au elementele în ordine
# crescătoare.
print("\nExercitiul 1:")
def countRows(matrix):
    count = 0
    for row in matrix:
        if all(row[i] <= row[i + 1] for i in range(len(row) - 1)):
            count += 1
    return count

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 3, 2]
]

num_sorted_rows = countRows(matrix)
print("Numărul de linii cu elementele în ordine crescătoare:", num_sorted_rows)


# 2. Determinați coloanele unei matrice cu proprietatea că au cel mai mic element egal cu 5
print("\nExercitiul 2:")

def minColumns(matrix):
    columns = []
    for j in range(len(matrix[0])):
        min_element = matrix[0][j]
        for i in range(1, len(matrix)):  # Gasim cel mai mic element
            min_element = min(min_element, matrix[i][j])
        if min_element == 5:
            columns.append(j)
    return columns

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 5],
    [0, 5, 3, 1, 7],
    [4, 3, 2, 5, 1]
]

columns_with_smallest_5 = minColumns(matrix)
print("Coloanele cu cel mai mic element egal cu 5:", columns_with_smallest_5)


# 3. Implementați algoritmul de sortare prin metoda bulelor pentru a ordona fiecare linie a unei
# matrice
print("\nExercitiul 3:")

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break

def sortRows(matrix):
    sorted_matrix = []
    for row in matrix:
        sorted_row = row[:]  # Pentru a nu modifica matricea originală
        bubbleSort(sorted_row)
        sorted_matrix.append(sorted_row)
    return sorted_matrix

matrix = [
    [3, 1, 4, 2],
    [6, 8, 5, 7],
    [9, 11, 10, 12]
]

print("Matricea originala:")
for row in matrix:
    print(row)

sorted_matrix = sortRows(matrix)
print("Matricea sortată:")
for row in sorted_matrix:
    print(row)


# 4. Implementați algoritmul de sortare prin inserție pentru a ordona fiecare coloană a unei
# matrice

print("\nExercitiul 4:")
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def sortColumns(matrix):
    sorted_matrix = []
    for j in range(len(matrix[0])):
        column = [matrix[i][j] for i in range(len(matrix))]  # Extragem coloana j
        insertionSort(column)
        for i in range(len(matrix)):
            matrix[i][j] = column[i]
    return matrix

matrix = [
    [3, 3, 4],
    [6, 2, 15],
    [9, 11, 10]
]

print("Matricea originala:")
for row in matrix:
    print(row)
sorted_matrix = sortColumns(matrix)
print("Matricea sortată pe fiecare coloană:")
for row in sorted_matrix:
    print(row)


# 5. Scrieți o funcție recursivă pentru calculul cmmdc dintre două numere naturale nenule
print("\nExercitiul 5:")

def cmmdc(a, b):
    if b == 0:
        return a
    return cmmdc(b, a % b)

a = 48
b = 18
rezultat = cmmdc(a, b)
print("CMMDC dintre", a, "și", b, "este:", rezultat)


# 6. Fie A și B două matrice pătratice și n un număr natural nenul. Calculați 𝐴^𝑇
# , A+B, A*B și 𝐴^𝑛.
print("\nExercitiul 6:")

import numpy as np

# Matricele A și B
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Calculăm A^T
A_transpose = np.transpose(A)

# Calculăm A + B
sum_matrix = A + B

# Calculăm A * B
product_matrix = np.dot(A, B)

# Definim n
n = 2

# Calculăm A^n
power_matrix = np.linalg.matrix_power(A, n)

# Afișăm rezultatele
print("Matricea transpusă a lui A:")
print(A_transpose)

print("\nSuma matricelor A și B:")
print(sum_matrix)

print("\nProdusul matricelor A și B:")
print(product_matrix)

print("\nA ridicat la puterea", n, ":")
print(power_matrix)


# 7. Implementați algoritmul de sortare prin inserție în liste/vectori
print("\nExercitiul 7:")
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [14, 9, 11, 4, 6]
insertionSort(arr)
print("Lista sortată folosind sortarea prin inserție:")
print(arr)


# 8. Verificați proprietatea unei permutări de a fi permutarea identică.
print("\nExercitiul 8:")
def identicalPermutation(perm):
    n = len(perm)
    for i in range(n):
        if perm[i] != i:
            return False
    return True


perm1 = [0, 1, 2, 3, 4]
perm2 = [3, 1, 2, 0, 4]

print("Perm1 este permutarea identică:", identicalPermutation(perm1))
print("Perm2 este permutarea identică:", identicalPermutation(perm2))



# 9. Fie S mulțimea vectorilor binari de lungime 7. Calculați, prin generare aleatoare, o matrice
# A cu 20 de linii, vectori din S și un vector V cu 20 de elemente, fiecare 𝑉[𝑖] reprezentând
# calitatea liniei i din A, definită prin suma biților vectorului linie i.
print("\nExercitiul 9:")
import numpy as np

# Generăm matricea A cu 20 de linii, fiecare linie fiind un vector binar de lungime 7
A = np.random.randint(2, size=(20, 7))

# Calculăm vectorul V cu 20 de elemente, fiecare reprezentând suma biților din linia corespunzătoare din A
V = np.sum(A, axis=1)

# Afișăm matricea A și vectorul V
print("Matricea A:")
print(A)
print("\nVectorul V:")
print(V)


# 10. Fie A și V construite la 9. Aranjați liniile matricei A astfel încât elementele lui V să fie în
# ordine crescătoare.
print("\nExercitiul 10:")
