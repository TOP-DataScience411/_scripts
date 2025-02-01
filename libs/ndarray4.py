from numpy import arange, array


matrix = arange(1, 25).reshape(6, 4)

# >>> print(matrix)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]
#  [17 18 19 20]
#  [21 22 23 24]]


# >>> matrix[0]
# array([1, 2, 3, 4])
# >>>
# >>> matrix[0][0]
# np.int64(1)
# >>>
# >>> matrix[0][0] == matrix[0, 0]
# np.True_
# >>>
# >>> matrix[-1, -1]
# np.int64(24)

# >>> matrix[:, 0]
# array([ 1,  5,  9, 13, 17, 21])
# >>>
# >>> matrix[:, 1]
# array([ 2,  6, 10, 14, 18, 22])
# >>>
# >>> matrix[2:, 1]
# array([10, 14, 18, 22])
# >>>
# >>> matrix[2:, 1:]
# array([[10, 11, 12],
#        [14, 15, 16],
#        [18, 19, 20],
#        [22, 23, 24]])
# >>> 
# >>> matrix[2::2, 1:]
# array([[10, 11, 12],
#        [18, 19, 20]])


mask = array([
    [False, True,  True,  True],
    [False, False, True,  True],
    [False, False, False, True],
    [True,  False, False, False],
    [True,  True,  False, False],
    [True,  True,  True,  False],
])

# >>> matrix[mask]
# array([ 2,  3,  4,  7,  8, 12, 13, 17, 18, 21, 22, 23])

mask = array([
    [True, False, True, True],
    [True, False, True, True],
    [True, False, True, True],
    [True, False, True, True],
    [True, False, True, True],
    [True, False, True, True],
])

# >>> matrix[mask]
# array([ 1,  3,  4,  5,  7,  8,  9, 11, 12, 13, 15, 16, 17, 19, 20, 21, 23, 24])
# >>>
# >>> matrix[mask].reshape(6, 3)
# array([[ 1,  3,  4],
#        [ 5,  7,  8],
#        [ 9, 11, 12],
#        [13, 15, 16],
#        [17, 19, 20],
#        [21, 23, 24]])

