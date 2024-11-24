def recursive_func(start):
    print('начало выполнения тела функции')
    if start > 0:
        print(f'перед рекурсивным вызовом {start = }')
        res = recursive_func(start - 1)
        print(f'после рекурсивного вызова {res = }')
        return res
    else:
        print('последний рекурсивный вызов')
        return 0
    print('конец выполнения тела функции')


res = recursive_func(5)

