from numpy import ones, arange, array


vector1 = ones(5, dtype=int)
# >>> vector1
# array([1, 1, 1, 1, 1])
vector2 = array([1, 5, -1, 2, 9])
# >>> vector2
# array([ 1,  5, -1,  2,  9])
vector3 = arange(10, 33, 3)
# >>> vector3
# array([10, 13, 16, 19, 22, 25, 28, 31])
vector4 = array([2, 2, 2])

matrix1 = ones((4, 3), dtype=int)
# >>> matrix1
# array([[1, 1, 1],
#        [1, 1, 1],
#        [1, 1, 1],
#        [1, 1, 1]])
matrix2 = arange(1, 13).reshape(4, 3)
# >>> matrix2
# array([[ 1,  2,  3],
#        [ 4,  5,  6],
#        [ 7,  8,  9],
#        [10, 11, 12]])
matrix3 = arange(1, 10).reshape(3, 3)
# >>> matrix3
# array([[1, 2, 3],
#        [4, 5, 6],
#        [7, 8, 9]])


# >>> vector1 + vector2
# array([ 2,  6,  0,  3, 10])
# >>>
# >>> vector1 - vector2
# array([ 0, -4,  2, -1, -8])
# >>>
# >>> vector1 * vector2
# array([ 1,  5, -1,  2,  9])
# >>>
# >>> vector1 / vector2
# array([ 1.        ,  0.2       , -1.        ,  0.5       ,  0.11111111])

# >>> vector1 + vector3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: operands could not be broadcast together with shapes (5,) (8,)


# >>> matrix2 + matrix1
# array([[ 2,  3,  4],
#        [ 5,  6,  7],
#        [ 8,  9, 10],
#        [11, 12, 13]])
# >>>
# >>> matrix2 - matrix1
# array([[ 0,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11]])
# >>>
# >>> matrix2 * matrix2
# array([[  1,   4,   9],
#        [ 16,  25,  36],
#        [ 49,  64,  81],
#        [100, 121, 144]])
# >>>
# >>> matrix1 / matrix2
# array([[1.        , 0.5       , 0.33333333],
#        [0.25      , 0.2       , 0.16666667],
#        [0.14285714, 0.125     , 0.11111111],
#        [0.1       , 0.09090909, 0.08333333]])


# >>> matrix1 + matrix3
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: operands could not be broadcast together with shapes (4,3) (3,3)


# >>> vector3 + matrix3
# array([[ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11]])
# >>>
# >>> array([vector3, vector3, vector3])
# array([[2, 2, 2],
#        [2, 2, 2],
#        [2, 2, 2]])


# >>> matrix3 + array([2, 2, 2, 2])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: operands could not be broadcast together with shapes (3,3) (4,)


# >>> vector2 + 10
# array([11, 15,  9, 12, 19])
# >>>
# >>> vector2 - 10
# array([ -9,  -5, -11,  -8,  -1])
# >>>
# >>> vector2 * 10
# array([ 10,  50, -10,  20,  90])
# >>>
# >>> vector2 / 10
# array([ 0.1,  0.5, -0.1,  0.2,  0.9])

