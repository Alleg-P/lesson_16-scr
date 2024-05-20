# Задача 3: Роман планирует акции

def calculate_discounts(shelves):
    discounts = []
    for i in range(len(shelves)):
        discount = [(i + 1) * shelves[i][1]] * shelves[i][1]
        discounts.append(discount)
    
    return discounts

shelves1 = [[4, 2], [5, 3], [6, 5]]
shelves2 = [[3, 1], [4, 4]]

discounts1 = calculate_discounts(shelves1)
discounts2 = calculate_discounts(shelves2)

print("Скидки:", discounts1)
print("Скидки:", discounts2)
