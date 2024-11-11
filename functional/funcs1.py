# def имя_функции(параметры_функции, ...):
#     тело_функции
#     ...


# def имя_функции(
#         строго_позиционные_параметры, 
#         ...,
#         позиционно_ключевые_параметры, 
#         ...,
#         произвольный_набор_позиционных_параметров,
#         строго_ключевые_параметры,
#         ...,
#         произвольный_набор_ключевых_параметров,
# ):
#     тело_функции
#     ...


print('вывод из основного модуля до объявления функции')


def test_func():
    print('вывод из тела функции')


print('вывод из основного модуля после объявления функции')

# вызов функции
test_func()

print('вывод из основного модуля после вызова функции')


# >>> test_func
# <function test_func at 0x0000017C5999A200>
# >>>
# >>> a = test_func
# >>> a
# <function test_func at 0x0000017C5999A200>
# >>>
# >>> a()
# вывод из тела функции
# >>>
# >>> test_func.__name__
# 'test_func'
# >>>
# >>> a.__name__
# 'test_func'


# >>> test_func.__doc__
# >>>
# >>> print.__doc__
# 'Prints the values to a stream, or to sys.stdout by default.\n\n  sep\n    string inserted between values, default a space.\n  end\n    string appended after the last value, default a newline.\n  file\n    a file-like object (stream); defaults to the current sys.stdout.\n  flush\n    whether to forcibly flush the stream.'
# >>>
# >>> print(print.__doc__)
# Prints the values to a stream, or to sys.stdout by default.
# 
#   sep
#     string inserted between values, default a space.
#   end
#     string appended after the last value, default a newline.
#   file
#     a file-like object (stream); defaults to the current sys.stdout.
#   flush
#     whether to forcibly flush the stream.
# >>>

