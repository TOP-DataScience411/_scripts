n, m = 4, 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

for i in range(n):
    for j in range(m):
        print(f'{i = }\t{j = }\t{matrix[i][j] = }')

# i = 0   j = 0   matrix[i][j] = 1
# i = 0   j = 1   matrix[i][j] = 2
# i = 0   j = 2   matrix[i][j] = 3
# i = 1   j = 0   matrix[i][j] = 4
# i = 1   j = 1   matrix[i][j] = 5
# i = 1   j = 2   matrix[i][j] = 6
# i = 2   j = 0   matrix[i][j] = 7
# i = 2   j = 1   matrix[i][j] = 8
# i = 2   j = 2   matrix[i][j] = 9
# i = 3   j = 0   matrix[i][j] = 10
# i = 3   j = 1   matrix[i][j] = 11
# i = 3   j = 2   matrix[i][j] = 12

