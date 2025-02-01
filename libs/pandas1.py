from numpy import linspace
from pandas import Series

from random import uniform


col1 = Series(
    data=range(10, 100, 10), 
    name='column_1'
)
# >>> col1
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# 5    60
# 6    70
# 7    80
# 8    90
# Name: column_1, dtype: int64


# >>> Series(data=range(10, 100, 10), dtype=float)
# 0    10.0
# 1    20.0
# 2    30.0
# 3    40.0
# 4    50.0
# 5    60.0
# 6    70.0
# 7    80.0
# 8    90.0
# dtype: float64


col2 = Series(
    data=range(10, 100, 10), 
    index=[f'row_{i}' for i in range(1, 10)],
    name='column_2'
)
# >>> col2
# row_1    10
# row_2    20
# row_3    30
# row_4    40
# row_5    50
# row_6    60
# row_7    70
# row_8    80
# row_9    90
# Name: column_2, dtype: int64


col3 = Series(
    data={
        f'x: {n}': f'y: {uniform(-5, 5):.3f}'
        for n in linspace(1, 10, 19)
    },
    name='column_3'
)
# >>> col3
# x: 1.0     y: -4.562
# x: 1.5     y: -4.678
# x: 2.0     y: -3.440
# x: 2.5     y: -4.890
# x: 3.0      y: 2.754
# x: 3.5      y: 0.781
# x: 4.0      y: 1.986
# x: 4.5     y: -3.861
# x: 5.0     y: -2.785
# x: 5.5      y: 3.760
# x: 6.0     y: -1.799
# x: 6.5     y: -0.999
# x: 7.0     y: -3.940
# x: 7.5     y: -1.956
# x: 8.0      y: 3.326
# x: 8.5     y: -4.028
# x: 9.0     y: -2.725
# x: 9.5      y: 4.593
# x: 10.0    y: -1.333
# Name: column_3, dtype: object


# >>> Series(data=[1, 2], index=[1, 2, 3, 4])
# ...
# ValueError: Length of values (2) does not match length of index (4)


# >>> col1.values
# array([10, 20, 30, 40, 50, 60, 70, 80, 90])
# >>>
# >>> col1.index
# RangeIndex(start=0, stop=9, step=1)
# >>>
# >>> col1.index.values
# array([0, 1, 2, 3, 4, 5, 6, 7, 8])

# >>> col2.values
# array([10, 20, 30, 40, 50, 60, 70, 80, 90])
# >>>
# >>> col2.index
# Index(['row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6', 'row_7', 'row_8',
#        'row_9'],
#       dtype='object')
# >>>
# >>> col2.index.values
# array(['row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6', 'row_7',
#        'row_8', 'row_9'], dtype=object)

# >>> col3.values
# array(['y: -4.562', 'y: -4.678', 'y: -3.440', 'y: -4.890', 'y: 2.754',
#        'y: 0.781', 'y: 1.986', 'y: -3.861', 'y: -2.785', 'y: 3.760',
#        'y: -1.799', 'y: -0.999', 'y: -3.940', 'y: -1.956', 'y: 3.326',
#        'y: -4.028', 'y: -2.725', 'y: 4.593', 'y: -1.333'], dtype=object)
# >>>
# >>> col3.index
# Index(['x: 1.0', 'x: 1.5', 'x: 2.0', 'x: 2.5', 'x: 3.0', 'x: 3.5', 'x: 4.0',
#        'x: 4.5', 'x: 5.0', 'x: 5.5', 'x: 6.0', 'x: 6.5', 'x: 7.0', 'x: 7.5',
#        'x: 8.0', 'x: 8.5', 'x: 9.0', 'x: 9.5', 'x: 10.0'],
#       dtype='object')
# >>>
# >>> col3.index.values
# array(['x: 1.0', 'x: 1.5', 'x: 2.0', 'x: 2.5', 'x: 3.0', 'x: 3.5',
#        'x: 4.0', 'x: 4.5', 'x: 5.0', 'x: 5.5', 'x: 6.0', 'x: 6.5',
#        'x: 7.0', 'x: 7.5', 'x: 8.0', 'x: 8.5', 'x: 9.0', 'x: 9.5',
#        'x: 10.0'], dtype=object)


# >>> col1[4]
# np.int64(50)
# >>>
# >>> col2['row_4']
# np.int64(40)
# >>>
# >>> col3['x: 4.5']
# 'y: -3.861'

