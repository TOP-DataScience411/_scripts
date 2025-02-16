from numpy import array, arange, diag, eye, zeros, dot


matr1 = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])
# matr1_ = arange(1, 10).reshape(3, 3)

matr2 = array([
    [-2, 0, 0],
    [0, 10, 0],
    [0, 0, 0],
])
# matr2_ = diag([-2, 10, 0])

matr3 = array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])
# matr3_ = eye(3, dtype=int)


# трансляция скаляра в матрицу, поэлементное сложение
# >>> matr1 + 10
# array([[11, 12, 13],
#        [14, 15, 16],
#        [17, 18, 19]])

# сдвиг — умножение скаляра на матрицу, поэлементное сложение
# >>> matr1 + 10*eye(3, dtype=int)
# array([[11,  2,  3],
#        [ 4, 15,  6],
#        [ 7,  8, 19]])


result1 = zeros((3, 3), dtype=int)

for i in range(matr1.shape[0]):
    for j in range(matr2.shape[1]):
        result1[i, j] = dot(matr1[i, :], matr2[:, j])

# >>> result1
# array([[ -2,  20,   0],
#        [ -8,  50,   0],
#        [-14,  80,   0]])


# >>> dot(matr1, matr2)
# array([[ -2,  20,   0],
#        [ -8,  50,   0],
#        [-14,  80,   0]])


# предпочтительный способ умножения матриц
# >>> matr1 @ matr2
# array([[ -2,  20,   0],
#        [ -8,  50,   0],
#        [-14,  80,   0]])


vect_r = arange(3, 10, 3).reshape(1, 3)
vect_c = arange(3, 10, 3).reshape(3, 1)

# >>> vect_r @ matr2
# array([[-6, 60,  0]])
# >>>
# >>> matr2 @ vect_c
# array([[-6],
#        [60],
#        [ 0]])

# >>> matr2 @ vect_r
# ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 1 is different from 3)
# >>>
# >>> vect_c @ matr2
# ValueError: matmul: Input operand 1 has a mismatch in its core dimension 0, with gufunc signature (n?,k),(k,m?)->(n?,m?) (size 3 is different from 1)


# матричное умножение — некоммутативная операция

# >>> matr1 @ matr2
# array([[ -2,  20,   0],
#        [ -8,  50,   0],
#        [-14,  80,   0]])
# >>>
# >>> matr2 @ matr1
# array([[-2, -4, -6],
#        [40, 50, 60],
#        [ 0,  0,  0]])



