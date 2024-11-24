data1 = [
    (1, 2, 3),
    (4, 5, 6),
]
data2 = [
    [
        (1, 2, 3),
        (4, 5, 6),
    ],
    [
        (7, 8, 9),
        (10, 11, 12),
    ],
]
data3 = [
    (
        [
            {1, 2, 3},
            {4, 5, 6},
        ],
        [
            {7, 8, 9},
            {10, 11, 12},
        ],
    ),
    (
        [
            {13, 14, 15},
            {16, 17, 18},
        ],
        [
            {19, 20, 21},
            {22, 23, 24},
        ],
    ),
]


def flatten(iterable):
    breakpoint()
    res = []
    for elem in iterable:
        if (
                type(elem) is list or
                type(elem) is tuple or
                type(elem) is set
        ):
            res.extend(flatten(elem))
        else:
            res.append(elem)
    return res


for struct in (data1, data2, data3):
    print(flatten(struct))

# > recursion3.py(42) flatten()
#   -> res = []
# 
# (Pdb) where
# 
#   recursion3.py(56) <module>()
#   -> print(flatten(struct))
# 
# > recursion3.py(42) flatten()
#   -> res = []
# 
# (Pdb) args
# iterable = [(1, 2, 3), (4, 5, 6)]
# 
# (Pdb) step
# 
# > recursion3.py(43) flatten()
#   -> for elem in iterable:
# 
# (Pdb) step
# 
# > recursion3.py(45) flatten()
#   -> type(elem) is list or
# 
# (Pdb) step
# 
# > recursion3.py(46) flatten()
#   -> type(elem) is tuple or
# 
# (Pdb) step
# 
# > recursion3.py(49) flatten()
#   -> res.extend(flatten(elem))
# 
# (Pdb) step
# 
# --Call--
# > recursion3.py(40) flatten()
#   -> def flatten(iterable):
# 
# (Pdb) args
# iterable = (1, 2, 3)
# 
# (Pdb) where
# 
#   recursion3.py(56) <module>()
#   -> print(flatten(struct))
# 
#   recursion3.py(49) flatten()
#   -> res.extend(flatten(elem))
# 
# > recursion3.py(40) flatten()
#   -> def flatten(iterable):
# 
# (Pdb) step
# 
# > recursion3.py(41) flatten()
#   -> breakpoint()
# 
# (Pdb) next
# 
# > recursion3.py(42) flatten()
#   -> res = []
# 
# (Pdb) step
# 
# > recursion3.py(43) flatten()
#   -> for elem in iterable:
# 
# (Pdb)
# 
# > recursion3.py(45) flatten()
#   -> type(elem) is list or
# 
# (Pdb)
# 
# > recursion3.py(46) flatten()
#   -> type(elem) is tuple or
# 
# (Pdb)
# 
# > recursion3.py(47) flatten()
#   -> type(elem) is set
# 
# (Pdb)
# 
# > recursion3.py(51) flatten()
#   -> res.append(elem)
# 
# (Pdb) res
# []
# 
# (Pdb) step
# 
# > recursion3.py(43) flatten()
#   -> for elem in iterable:
# 
# (Pdb) res
# [1]
# 
# (Pdb) step
# 
# > recursion3.py(45) flatten()
#   -> type(elem) is list or
# 
# (Pdb)
# 
# > recursion3.py(46) flatten()
#   -> type(elem) is tuple or
# 
# (Pdb)
# 
# > recursion3.py(47) flatten()
#   -> type(elem) is set
# 
# (Pdb)
# 
# > recursion3.py(51) flatten()
#   -> res.append(elem)
# 
# (Pdb)
# 
# > recursion3.py(43) flatten()
#   -> for elem in iterable:
# 
# (Pdb)
# 
# > recursion3.py(45) flatten()
#   -> type(elem) is list or
# 
# (Pdb)
# 
# > recursion3.py(46) flatten()
#   -> type(elem) is tuple or
# 
# (Pdb)
# 
# > recursion3.py(47) flatten()
#   -> type(elem) is set
# 
# (Pdb)
# 
# > recursion3.py(51) flatten()
#   -> res.append(elem)
# 
# (Pdb)
# 
# > recursion3.py(43) flatten()
#   -> for elem in iterable:
# 
# (Pdb)
# 
# > recursion3.py(52) flatten()
#   -> return res
# 
# (Pdb) where
# 
#   recursion3.py(56) <module>()
#   -> print(flatten(struct))
# 
#   recursion3.py(49) flatten()
#   -> res.extend(flatten(elem))
# 
# > recursion3.py(52) flatten()
#   -> return res
# 
# (Pdb) res
# [1, 2, 3]
# 
# (Pdb) step
# 
# --Return--
# > recursion3.py(52) flatten()-->[1, 2, 3]
#   -> return res
# 
# (Pdb)
# 
# > recursion3.py(43) flatten()
#   -> for elem in iterable:
# 
# (Pdb) where
# 
#   recursion3.py(56) <module>()
#   -> print(flatten(struct))
# 
# > recursion3.py(43) flatten()
#   -> for elem in iterable:
# 
# (Pdb) elem
# (1, 2, 3)
# 
# (Pdb) step
# 
# > recursion3.py(45) flatten()
#   -> type(elem) is list or
# 
# (Pdb) elem
# (4, 5, 6)
# 
# (Pdb) step
# 
# > recursion3.py(46) flatten()
#   -> type(elem) is tuple or
# 
# (Pdb)
# 
# > recursion3.py(49) flatten()
#   -> res.extend(flatten(elem))
# 
# (Pdb)
# 
# --Call--
# > recursion3.py(40) flatten()
#   -> def flatten(iterable):
# 
# (Pdb) args
# iterable = (4, 5, 6)
# 
# (Pdb) step
# 
# > recursion3.py(41) flatten()
#   -> breakpoint()
# 
# (Pdb) where
# 
#   recursion3.py(56) <module>()
#   -> print(flatten(struct))
# 
#   recursion3.py(49) flatten()
#   -> res.extend(flatten(elem))
# 
# > recursion3.py(41) flatten()
#   -> breakpoint()
# 
# (Pdb) next
# 
# > recursion3.py(42) flatten()
#   -> res = []
# 
# (Pdb) continue
# [1, 2, 3, 4, 5, 6]
# 
# > ...

