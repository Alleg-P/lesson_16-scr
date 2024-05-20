# Задача 1: Роман и оптимизации

example_data1 = {"num_of_shelves": 3, "shelf_lengths": [4, 5, 6]}
example_data2 = {"num_of_shelves": 2, "shelf_lengths": [3, 4]}

def create_shelves(num_of_shelves, shelf_lengths):
    shelves = []
    
    for length in shelf_lengths:
        shelves.append([length, 0])
    
    return shelves

shelves1 = create_shelves(**example_data1)
print("Полки:", shelves1)

shelves2 = create_shelves(**example_data2)
print("Полки:", shelves2)
