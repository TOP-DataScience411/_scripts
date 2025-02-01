from numpy import array


vector = [1, 0, 3, 2, 0, 8, 1]
vector_np = array(vector)

# >>> type(vector_np)
# <class 'numpy.ndarray'>

# >>> vector_np
# array([1, 0, 3, 2, 0, 8, 1])
# >>>
# >>> print(vector_np)
# [1 0 3 2 0 8 1]
# >>> 
# >>> vector_np.shape
# (7,)

vector_np_oriented = array([vector])

# >>> vector_np_oriented
# array([[1, 0, 3, 2, 0, 8, 1]])
# >>>
# >>> vector_np_oriented.shape
# (1, 7)
# >>>
# >>> vector_np_oriented.T
# array([[1],
#        [0],
#        [3],
#        [2],
#        [0],
#        [8],
#        [1]])
# >>>
# >>> vector_np_oriented.T.shape
# (7, 1)

matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
]
matrix_np = array(matrix)

# >>> matrix_np
# array([[1, 0, 0],
#        [0, 1, 0],
#        [0, 0, 1]])
# >>>
# >>> print(matrix_np)
# [[1 0 0]
#  [0 1 0]
#  [0 0 1]]
# >>>
# >>> matrix_np.shape
# (3, 3)

matrix_np2 = array([
    [1, 2, 3],
    [4, 5, 6]
])

# >>> matrix_np2.shape
# (2, 3)
# >>>
# >>> matrix_np2.T
# array([[1, 4],
#        [2, 5],
#        [3, 6]])
# >>>
# >>> matrix_np2.T.shape
# (3, 2)

matrix_np3 = array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],
    [[100, 110, 120, 130],
     [200, 210, 220, 230],
     [300, 310, 320, 330]],
])

# >>> matrix_np3
# array([[[  1,   2,   3,   4],
#         [  5,   6,   7,   8],
#         [  9,  10,  11,  12]],
# 
#        [[100, 110, 120, 130],
#         [200, 210, 220, 230],
#         [300, 310, 320, 330]]])
# >>>
# >>> matrix_np3.shape
# (2, 3, 4)
# >>>
# >>> matrix_np3.T
# array([[[  1, 100],
#         [  5, 200],
#         [  9, 300]],
# 
#        [[  2, 110],
#         [  6, 210],
#         [ 10, 310]],
# 
#        [[  3, 120],
#         [  7, 220],
#         [ 11, 320]],
# 
#        [[  4, 130],
#         [  8, 230],
#         [ 12, 330]]])
# >>>
# >>> matrix_np3.T.shape
# (4, 3, 2)

