from numpy.random import default_rng


generator = default_rng()

# >>> generator.integers(10, 100)
# np.int64(64)
# >>>
# >>> generator.integers(10, 100, 5)
# array([49, 70, 45, 86, 75])
# >>>
# >>> generator.integers(10, 100, (5, 5))
# array([[14, 62, 10, 43, 10],
#        [73, 96, 18, 57, 58],
#        [82, 82, 60, 30, 50],
#        [51, 52, 85, 35, 73],
#        [70, 35, 97, 27, 93]])
# >>>
# >>> generator.integers(10, 100, (2, 3, 4))
# array([[[93, 11, 45, 52],
#         [59, 79, 55, 60],
#         [77, 36, 67, 11]],
# 
#        [[60, 48, 67, 44],
#         [17, 56, 16, 33],
#         [67, 82, 12, 90]]])


# >>> generator = default_rng(123456789)
# >>>
# >>> generator.integers(10, 100, 5)
# array([91, 12, 62, 91, 40])
# >>>
# >>> generator.integers(10, 100, 5)
# array([89, 36, 66, 21, 81])


# >>> generator = default_rng(123456789)
# >>>
# >>> generator.integers(10, 100, 5)
# array([91, 12, 62, 91, 40])
# >>>
# >>> generator.integers(10, 100, 5)
# array([89, 36, 66, 21, 81])


# >>> generator = default_rng(1)
# >>>
# >>> generator.integers(10, 100, 5)
# array([52, 56, 77, 95, 13])
# >>>
# >>> generator.integers(10, 100, 5)
# array([22, 84, 95, 32, 38])


# >>> generator = default_rng(123456789)
# >>>
# >>> generator.integers(10, 100, 5)
# array([91, 12, 62, 91, 40])
# >>>
# >>> generator.integers(10, 100, 5)
# array([89, 36, 66, 21, 81])


#  > python -i ndarray6.py
# >>>
# >>> generator = default_rng(123456789)
# >>>
# >>> generator.integers(10, 100, 5)
# array([91, 12, 62, 91, 40])
# >>>
# >>> generator.integers(10, 100, 5)
# array([89, 36, 66, 21, 81])

