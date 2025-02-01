from pandas import DataFrame

from random import randrange as rr


table = DataFrame(
    data={
        f'col_{i}': [rr(10, 100) for _ in range(12)]
        for i in range(1, 6)
    }
)
# >>> table
#     col_1  col_2  col_3  col_4  col_5
# 0      63     88     70     68     66
# 1      65     98     63     26     48
# 2      83     13     52     65     23
# 3      79     34     21     44     30
# 4      18     89     50     64     51
# 5      36     53     37     41     82
# 6      43     71     42     35     48
# 7      80     32     22     38     67
# 8      69     85     60     91     67
# 9      49     13     15     64     44
# 10     53     87     37     87     13
# 11     62     87     46     74     88


# >>> table.loc
# <pandas.core.indexing._LocIndexer object at 0x00000165B8582B70>
# >>>
# >>>
# >>> table.loc[0]
# col_1    63
# col_2    88
# col_3    70
# col_4    68
# col_5    66
# Name: 0, dtype: int64
# >>>
# >>> type(table.loc[0])
# <class 'pandas.core.series.Series'>
# >>>
# >>> table.loc[0].index
# Index(['col_1', 'col_2', 'col_3', 'col_4', 'col_5'], dtype='object')
# >>>
# >>>
# >>> table.loc[0, 'col_3']
# np.int64(70)
# >>>
# >>> table.loc[0, ['col_2', 'col_4']]
# col_2    88
# col_4    68
# Name: 0, dtype: int64
# >>>
# >>> table.loc[5:10, 'col_2']
# 5     53
# 6     71
# 7     32
# 8     85
# 9     13
# 10    87
# Name: col_2, dtype: int64
# >>>
# >>> table.loc[:5, 'col_1':'col_3']
#    col_1  col_2  col_3
# 0     63     88     70
# 1     65     98     63
# 2     83     13     52
# 3     79     34     21
# 4     18     89     50
# 5     36     53     37


# >>> table.index = [i/10 for i in range(1, 13)]
# >>> table
#      col_1  col_2  col_3  col_4  col_5
# 0.1     63     88     70     68     66
# 0.2     65     98     63     26     48
# 0.3     83     13     52     65     23
# 0.4     79     34     21     44     30
# 0.5     18     89     50     64     51
# 0.6     36     53     37     41     82
# 0.7     43     71     42     35     48
# 0.8     80     32     22     38     67
# 0.9     69     85     60     91     67
# 1.0     49     13     15     64     44
# 1.1     53     87     37     87     13
# 1.2     62     87     46     74     88
# >>>
# >>> table.index
# Index([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2], dtype='float64')


# >>> table.shape
# (12, 5)
# >>>
# >>> table.info()
# <class 'pandas.core.frame.DataFrame'>
# Index: 12 entries, 0.1 to 1.2
# Data columns (total 5 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   col_1   12 non-null     int64
#  1   col_2   12 non-null     int64
#  2   col_3   12 non-null     int64
#  3   col_4   12 non-null     int64
#  4   col_5   12 non-null     int64
# dtypes: int64(5)
# memory usage: 576.0 bytes


# >>> table['col_1'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# >>> table
#      col_1  col_2  col_3  col_4  col_5
# 0.1      1     88     70     68     66
# 0.2      2     98     63     26     48
# 0.3      3     13     52     65     23
# 0.4      4     34     21     44     30
# 0.5      5     89     50     64     51
# 0.6      6     53     37     41     82
# 0.7      7     71     42     35     48
# 0.8      8     32     22     38     67
# 0.9      9     85     60     91     67
# 1.0     10     13     15     64     44
# 1.1     11     87     37     87     13
# 1.2     12     87     46     74     88
# >>>
# >>> table.loc[0.1] = [10, 20, 30, 40, 50]
# >>> table
#      col_1  col_2  col_3  col_4  col_5
# 0.1     10     20     30     40     50
# 0.2      2     98     63     26     48
# 0.3      3     13     52     65     23
# 0.4      4     34     21     44     30
# 0.5      5     89     50     64     51
# 0.6      6     53     37     41     82
# 0.7      7     71     42     35     48
# 0.8      8     32     22     38     67
# 0.9      9     85     60     91     67
# 1.0     10     13     15     64     44
# 1.1     11     87     37     87     13
# 1.2     12     87     46     74     88


# >>> table.T
#        0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0  1.1  1.2
# col_1   10    2    3    4    5    6    7    8    9   10   11   12
# col_2   20   98   13   34   89   53   71   32   85   13   87   87
# col_3   30   63   52   21   50   37   42   22   60   15   37   46
# col_4   40   26   65   44   64   41   35   38   91   64   87   74
# col_5   50   48   23   30   51   82   48   67   67   44   13   88

