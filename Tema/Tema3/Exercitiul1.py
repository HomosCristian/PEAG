import numpy as np

# 1. Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓:{(𝑥, 𝑦, 𝑧)⁄𝑥, 𝑦, 𝑧 ∈ [−2,7], 𝑥 + 𝑦 + 𝑧 < 10} → ℝ
# 𝑓(𝑥, 𝑦, 𝑧) = 𝑥^2 - 2y*z
# Generați 20 elemente din spațiul soluțiilor (candidați la soluție), evaluați-le și afișați valorile obținute.

def fmax(x, y, z):
    return x**2 - 2*y*z

# Generarea celor 20 de valori
x_values = np.random.uniform(-2, 7, 20)
y_values = np.random.uniform(-2, 7, 20)
z_values = np.random.uniform(-2, 7, 20)

# Evaluarea functiei
print("Exercitiul 1:")
for i in range(20):
    x = x_values[i]
    y = y_values[i]
    z = z_values[i]
    if x + y + z < 10:
        result = fmax(x, y, z)
        print(f"f({x}, {y}, {z}) = {result}")