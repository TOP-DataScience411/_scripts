def test_func(*args):
    print(
        type(args),
        len(args),
        args,
        sep='\n'
    )


# >>> test_func()
# <class 'tuple'>
# 0
# ()
# >>>
# >>> test_func('abc')
# <class 'tuple'>
# 1
# ('abc',)
# >>>
# >>> test_func('abc', 2, 'def')
# <class 'tuple'>
# 3
# ('abc', 2, 'def')


def test_func(pos1, pos2, *positional, key1):
    print(
        f'{pos1 = }\n'
        f'{pos2 = }\n'
        f'{positional = }\n'
        f'{key1 = }'
    )


# >>> test_func()
# TypeError: test_func() missing 2 required positional arguments: 'pos1' and 'pos2'
# >>>
# >>> test_func(1, 2)
# TypeError: test_func() missing 1 required keyword-only argument: 'key1'
# >>>
# >>> test_func(1, 2, key1=10)
# pos1 = 1
# pos2 = 2
# positional = ()
# key1 = 10


# >>> test_func(1, 2, 3, 4, key1=10)
# pos1 = 1
# pos2 = 2
# positional = (3, 4)
# key1 = 10


# >>> nums = list(range(10, 100, 10))
# >>> nums
# [10, 20, 30, 40, 50, 60, 70, 80, 90]
# >>>
# >>> test_func(*nums)
# TypeError: test_func() missing 1 required keyword-only argument: 'key1'
# >>>
# >>> test_func(*nums, key1='abc')
# pos1 = 10
# pos2 = 20
# positional = (30, 40, 50, 60, 70, 80, 90)
# key1 = 'abc'

