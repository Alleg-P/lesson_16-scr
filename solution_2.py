# Задача 2: Распределение товаров по полкам

def update_shelves(shelves, quantities):
    for i, quantity in enumerate(quantities):
        shelves[i][1] = quantity

shelves1 = [[4, 0], [5, 0], [6, 0]]
quantities1 = [2, 3, 5]

update_shelves(shelves1, quantities1)

print("Полки:", shelves1)

shelves2 = [[3, 0], [4, 0]]
quantities2 = [1, 4]

update_shelves(shelves2, quantities2)

print("Полки:", shelves2)
