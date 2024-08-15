import pulp

# Створюємо проблему лінійного програмування для максимізації
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні: кількість вироблених одиниць Лимонаду і Фруктового соку
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Integer')

# Функція цілі: максимізація загальної кількості продуктів
problem += lemonade + fruit_juice, "Total Products"

# Обмеження на ресурси
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water Constraint"
problem += 1 * lemonade <= 50, "Sugar Constraint"
problem += 1 * lemonade <= 30, "Lemon Juice Constraint"
problem += 2 * fruit_juice <= 40, "Fruit Puree Constraint"

# Розв'язання проблеми
problem.solve()

# Результати
print("Status:", pulp.LpStatus[problem.status])
print("Optimal production of Lemonade:", lemonade.varValue)
print("Optimal production of Fruit Juice:", fruit_juice.varValue)
print("Total Products:", pulp.value(problem.objective))
