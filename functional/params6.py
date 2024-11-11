def test_func(**kwargs):
    print(
        type(kwargs),
        len(kwargs),
        kwargs,
        sep='\n'
    )


# >>> test_func()
# <class 'dict'>
# 0
# {}
# >>>
# >>>
# >>> test_func(10, 43)
# TypeError: test_func() takes 0 positional arguments but 2 were given
# >>>
# >>>
# >>> test_func(key1=10, ключ2=43)
# <class 'dict'>
# 2
# {'key1': 10, 'ключ2': 43}


def test_func2(pos, *positionals, key1, key2='default', **keywords):
    pass

