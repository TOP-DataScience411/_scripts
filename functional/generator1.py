def generator_function():
    print('начало выполнения тела генераторной функции')
    yield 2
    print('следующий шаг выполнения тела генераторной функции')
    yield 3
    print('следующий шаг выполнения тела генераторной функции')
    yield 5
    print('следующий шаг выполнения тела генераторной функции')
    yield 8
    print('конец выполнения тела генераторной функции')


generator_object = generator_function()

# >>> generator_object
# <generator object generator_function at 0x0000023F576B56C0>
# >>>
# >>> type(generator_object)
# <class 'generator'>


# >>> generator_object.__next__()
# начало выполнения тела генераторной функции
# 2
# >>> var = generator_object.__next__()
# следующий шаг выполнения тела генераторной функции
# >>> var
# 3
# >>> var = generator_object.__next__()
# следующий шаг выполнения тела генераторной функции
# >>> var
# 5
# >>> generator_object.__next__()
# следующий шаг выполнения тела генераторной функции
# 8
# >>> generator_object.__next__()
# конец выполнения тела генераторной функции
# StopIteration
# >>>
# >>> generator_object.__next__()
# StopIteration


for var in generator_object:
    print(var)

# начало выполнения тела генераторной функции
# 2
# следующий шаг выполнения тела генераторной функции
# 3
# следующий шаг выполнения тела генераторной функции
# 5
# следующий шаг выполнения тела генераторной функции
# 8
# конец выполнения тела генераторной функции

# >>> var
# 8

