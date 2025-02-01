from pandas import DataFrame

from random import randrange as rr


table1 = DataFrame(
    data=[range(i, i+100, 10) for i in range(10)]
)
# >>> table1
#    0   1   2   3   4   5   6   7   8   9
# 0  0  10  20  30  40  50  60  70  80  90
# 1  1  11  21  31  41  51  61  71  81  91
# 2  2  12  22  32  42  52  62  72  82  92
# 3  3  13  23  33  43  53  63  73  83  93
# 4  4  14  24  34  44  54  64  74  84  94
# 5  5  15  25  35  45  55  65  75  85  95
# 6  6  16  26  36  46  56  66  76  86  96
# 7  7  17  27  37  47  57  67  77  87  97
# 8  8  18  28  38  48  58  68  78  88  98
# 9  9  19  29  39  49  59  69  79  89  99
# >>>
# >>> table1.index
# RangeIndex(start=0, stop=10, step=1)
# >>>
# >>> table1.columns
# RangeIndex(start=0, stop=10, step=1)


table2 = DataFrame(
    data=[range(i, i+100, 10) for i in range(10)],
    index=[f'row_{i}' for i in range(1, 11)]
)
# >>> table2
#         0   1   2   3   4   5   6   7   8   9
# row_1   0  10  20  30  40  50  60  70  80  90
# row_2   1  11  21  31  41  51  61  71  81  91
# row_3   2  12  22  32  42  52  62  72  82  92
# row_4   3  13  23  33  43  53  63  73  83  93
# row_5   4  14  24  34  44  54  64  74  84  94
# row_6   5  15  25  35  45  55  65  75  85  95
# row_7   6  16  26  36  46  56  66  76  86  96
# row_8   7  17  27  37  47  57  67  77  87  97
# row_9   8  18  28  38  48  58  68  78  88  98
# row_10  9  19  29  39  49  59  69  79  89  99
# >>>
# >>> table2.index
# Index(['row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6', 'row_7', 'row_8',
#        'row_9', 'row_10'],
#       dtype='object')
# >>>
# >>> table2.columns
# RangeIndex(start=0, stop=10, step=1)


table3 = DataFrame(
    data=[range(i, i+100, 10) for i in range(10)],
    index=[f'row_{i}' for i in range(1, 11)],
    columns=[f'col_{i}' for i in range(1, 11)]
)
# >>> table3
#         col_1  col_2  col_3  col_4  col_5  col_6  col_7  col_8  col_9  col_10
# row_1       0     10     20     30     40     50     60     70     80      90
# row_2       1     11     21     31     41     51     61     71     81      91
# row_3       2     12     22     32     42     52     62     72     82      92
# row_4       3     13     23     33     43     53     63     73     83      93
# row_5       4     14     24     34     44     54     64     74     84      94
# row_6       5     15     25     35     45     55     65     75     85      95
# row_7       6     16     26     36     46     56     66     76     86      96
# row_8       7     17     27     37     47     57     67     77     87      97
# row_9       8     18     28     38     48     58     68     78     88      98
# row_10      9     19     29     39     49     59     69     79     89      99
# >>> table3.index
# Index(['row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6', 'row_7', 'row_8',
#        'row_9', 'row_10'],
#       dtype='object')
# >>>
# >>> table3.columns
# Index(['col_1', 'col_2', 'col_3', 'col_4', 'col_5', 'col_6', 'col_7', 'col_8',
#        'col_9', 'col_10'],
#       dtype='object')


table4 = DataFrame(
    data={
        f'col_{i}': [rr(10, 100) for _ in range(12)]
        for i in range(1, 6)
    }
)
# >>> table4
#     col_1  col_2  col_3  col_4  col_5
# 0      99     60     66     56     65
# 1      21     74     80     21     38
# 2      32     61     10     79     30
# 3      69     61     60     22     47
# 4      52     28     26     23     32
# 5      28     78     47     79     38
# 6      78     71     39     94     46
# 7      77     22     45     93     54
# 8      32     35     23     95     86
# 9      16     51     83     47     32
# 10     50     32     56     28     14
# 11     50     64     73     10     55


# >>> table3['col_1']
# row_1     0
# row_2     1
# row_3     2
# row_4     3
# row_5     4
# row_6     5
# row_7     6
# row_8     7
# row_9     8
# row_10    9
# Name: col_1, dtype: int64
# >>>
# >>> type(table3['col_1'])
# <class 'pandas.core.series.Series'>


# >>> table3['row_7']
# ...
# KeyError: 'row_7'


# >>> table3['col_1']
# row_1     0
# row_2     1
# row_3     2
# row_4     3
# row_5     4
# row_6     5
# row_7     6
# row_8     7
# row_9     8
# row_10    9
# Name: col_1, dtype: int64
# >>>
# >>> table3['col_1'].index
# Index(['row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6', 'row_7', 'row_8',
#        'row_9', 'row_10'],
#       dtype='object')
# >>>
# >>> table3['col_2']
# row_1     10
# row_2     11
# row_3     12
# row_4     13
# row_5     14
# row_6     15
# row_7     16
# row_8     17
# row_9     18
# row_10    19
# Name: col_2, dtype: int64
# >>>
# >>> table3['col_2'].index
# Index(['row_1', 'row_2', 'row_3', 'row_4', 'row_5', 'row_6', 'row_7', 'row_8',
#        'row_9', 'row_10'],
#       dtype='object')
# >>>
# >>> table3['col_1'].index == table3['col_2'].index
# array([ True,  True,  True,  True,  True,  True,  True,  True,  True,
#         True,  True,  True])

