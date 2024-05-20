# Задача 5: Спиральная матрица дизайна

def generate_spiral_matrix(n):
    matrix = [[0]*n for _ in range(n)]
    num = 1
    top = 0
    bottom = n-1
    left = 0
    right = n-1
    
    while num <= n*n:
        for i in range(left, right+1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        for i in range(top, bottom+1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        for i in range(right, left-1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top-1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    max_length = len(str(n * n))

    for row in matrix:
        for cell in row:
            print(str(cell).rjust(max_length), end=' ')
        print()

n = 3
generate_spiral_matrix(n)

n = 4
generate_spiral_matrix(n)
