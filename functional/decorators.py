def decorator(function_object):
    print('начало вызова декоратора')
    
    def wrapper_function(*args, **kwargs):
        print('начало вызова обёртки')
        result = function_object(*args, **kwargs)
        print('конец вызова обёртки')
        return result
    
    print('конец вызова декоратора')
    return wrapper_function


def test():
    print('вызов декорируемой функции')


test()

# test = decorator(test)
# test()

# >>> test
# <function test at 0x000001B4F68739C0>
# >>>
# >>> test.__name__
# 'test'
# >>>
# >>> test = decorator(test)
# начало вызова декоратора
# конец вызова декоратора
# >>>
# >>> test
# <function decorator.<locals>.wrapper_function at 0x000001B4F6873B00>
# >>>
# >>> test.__name__
# 'wrapper_function'
# >>>
# >>> test()
# начало вызова обёртки
# вызов декорируемой функции
# конец вызова обёртки

