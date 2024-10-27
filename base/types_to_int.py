print(f'int(5.2) -> {int(5.2)}')
print(f'int(1.9) -> {int(1.9)}')
print(f'int(False) -> {int(False)}')
print(f'int(True) -> {int(True)}')
print(f'int("4") -> {int("4")}')
print(f'int("-2") -> {int("-2")}')

# >>> int(None)
# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'
# >>>
# >>> int('1k5')
# ValueError: invalid literal for int() with base 10: '1k5'
# >>>
# >>> int('1.5')
# ValueError: invalid literal for int() with base 10: '1.5'
# >>>
# >>> int('4 3 1')
# ValueError: invalid literal for int() with base 10: '4 3 1'
# >>>
# >>> int(' 431  ')
# 431
# >>>
# >>> int('\n431 ')
# 431
# >>>
# >>> int('7-')
# ValueError: invalid literal for int() with base 10: '7-'
# >>>
# >>> int('7-2')
# ValueError: invalid literal for int() with base 10: '7-2'

