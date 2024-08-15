import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Обчислення інтеграла методом Монте-Карло
N = 1000000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = f(x_rand)
monte_carlo_result = (b - a) * np.mean(y_rand)

# Обчислення інтеграла за допомогою функції quad
quad_result, error = spi.quad(f, a, b)

# Аналітичний результат
analytical_result = (b**3 - a**3) / 3

# Виведення результатів
print(f"Метод Монте-Карло: {monte_carlo_result}")
print(f"Функція quad: {quad_result} (похибка {error})")
print(f"Аналітичний результат: {analytical_result}")

# Побудова графіка
import matplotlib.pyplot as plt

x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()
