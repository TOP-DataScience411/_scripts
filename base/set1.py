numbers_list = [1, 2, 5, 3, 1, 9, 3]
numbers_set = {1, 2, 5, 3, 1, 9, 3}

# >>> numbers_list
# [1, 2, 5, 3, 1, 9, 3]
# >>>
# >>> len(numbers_list)
# 7

# >>> numbers_set
# {1, 2, 3, 5, 9}
# >>>
# >>> len(numbers_set)
# 5

# >>> set(numbers_list)
# {1, 2, 3, 5, 9}
# >>>
# >>> set(numbers_list) == numbers_set
# True
# >>>
# >>> {1, 1} == {1}
# True

# >>> set(['abba'])
# {'abba'}
# >>>
# >>> set('abba')
# {'a', 'b'}

# >>> {(1, 2), 'abcd', range(10), frozenset([1, 2])}
# {frozenset({1, 2}), (1, 2), range(0, 10), 'abcd'}

# >>> {[1, 2], [3, 4]}
# TypeError: unhashable type: 'list'
# >>>
# >>> {{1, 3}, {2, 4}}
# TypeError: unhashable type: 'set'
# >>>
# >>> {{1: 3}, {2: 4}}
# TypeError: unhashable type: 'dict'

# >>> set()
# set()


# >>> {3, 5} == {5, 3}
# True
# >>>
# >>> {5, 10, 3} > {5, 3}
# True
# >>>
# >>> {5, 10, 3} > {3, 5}
# True
# >>>
# >>> {1} < {1, 2, 3}
# True
# >>>
# >>> {1, 2} < {1, 2, 3}
# True
# >>>
# >>> {1, 3} < {1, 2, 3}
# True
# >>>
# >>> {2, 3} < {1, 2, 3}
# True
# >>>
# >>> {1, 2, 3} < {1, 2, 3}
# False
# >>>
# >>> {1, 2, 3} <= {1, 2, 3}
# True

