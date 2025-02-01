from numpy import arange
from pandas import DataFrame


m1 = DataFrame(arange(1, 10).reshape(3, 3))
m2 = DataFrame(arange(10, 100, 10).reshape(3, 3))
m3 = DataFrame(arange(1, 13).reshape(4, 3))


# >>> m1 + m2
#     0   1   2
# 0  11  22  33
# 1  44  55  66
# 2  77  88  99
# >>>
# >>> m2 - m1
#     0   1   2
# 0   9  18  27
# 1  36  45  54
# 2  63  72  81
# >>>
# >>> m1 * m2
#      0    1    2
# 0   10   40   90
# 1  160  250  360
# 2  490  640  810
# >>>
# >>> m1 / m2
#      0    1    2
# 0  0.1  0.1  0.1
# 1  0.1  0.1  0.1
# 2  0.1  0.1  0.1
# >>>
# >>> m1 // m2
#    0  1  2
# 0  0  0  0
# 1  0  0  0
# 2  0  0  0


# >>> m1 + m3
#       0     1     2
# 0   2.0   4.0   6.0
# 1   8.0  10.0  12.0
# 2  14.0  16.0  18.0
# 3   NaN   NaN   NaN
# >>>
# >>> (m1 + m3).info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 4 entries, 0 to 3
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   0       3 non-null      float64
#  1   1       3 non-null      float64
#  2   2       3 non-null      float64
# dtypes: float64(3)
# memory usage: 128.0 bytes
# >>>
# >>> (m1 + m3).loc[3, 0]
# np.float64(nan)


# >>> m2 < m1
#        0      1      2
# 0  False  False  False
# 1  False  False  False
# 2  False  False  False
# >>>
# >>> m2 > m1
#       0     1     2
# 0  True  True  True
# 1  True  True  True
# 2  True  True  True
# >>>
# >>> (m2 > m1).all()
# 0    True
# 1    True
# 2    True
# dtype: bool
# >>>
# >>> (m2 > m1).all().all()
# np.True_
# >>>
# >>> (m2 > m1).all(None)
# np.True_

# >>> m1.loc[2, 2] = 900
# >>> m1
#    0  1    2
# 0  1  2    3
# 1  4  5    6
# 2  7  8  900
# >>>
# >>> m1 < m2
#       0     1      2
# 0  True  True   True
# 1  True  True   True
# 2  True  True  False
# >>>
# >>> (m1 < m2).all(None)
# np.False_

