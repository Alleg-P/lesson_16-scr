# Задача 4: Роман анализирует эффективность расположения товаров

def create_sales_matrix(num_shelves, sales_data):

    sales_matrix = [sales_data[i:i+num_shelves] for i in range(0, len(sales_data), num_shelves)]
    return sales_matrix

num_shelves_1 = 2
sales_data_1 = [5, 3, 7, 2]

num_shelves_2 = 3
sales_data_2 = [2, 6, 4, 3, 5, 7, 1, 2, 3]

print("Продажи:", create_sales_matrix(num_shelves_1, sales_data_1))
print("Продажи:", create_sales_matrix(num_shelves_2, sales_data_2))