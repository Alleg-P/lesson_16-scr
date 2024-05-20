# Задача 6: Оптимизация рабочих пространств

def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        matrix[i][n-1-i] = 5
        matrix[i][i] = 0
        for j in range(i+1, n-1-i):
            matrix[i][j] = 1
        for j in range(i+1, n-1-i):
            matrix[j][n-1-i] = 4
        for j in range(n-2-i, i, -1):
            matrix[n-1-i][j] = 3
        for j in range(n-2-i, i, -1):
            matrix[j][i] = 2
    
    return matrix

n = 3
matrix = create_matrix(n)

for row in matrix:
    print(' '.join(map(str, row)))

n = 5
matrix = create_matrix(n)

for row in matrix:
    print(' '.join(map(str, row)))
    