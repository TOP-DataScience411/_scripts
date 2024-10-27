print(f'float(6) = {float(6)}')
print(f'{float(6) = }')

print(f'{float(-1) = }')
print(f'{float(False) = }')
print(f'{float(True) = }')
print(f'{float('4') = }')
print(f'{float('5.4') = }')
print(f'{float('.9') = }')
print(f'{float('-1') = }')
print(f'{float('-9.1') = }')

# >>> float(None)
# TypeError: float() argument must be a string or a real number, not 'NoneType'
# >>>
# >>> float('4,5')
# ValueError: could not convert string to float: '4,5'
# >>>
# >>> float('4 5')
# ValueError: could not convert string to float: '4 5'
# >>>
# >>> float('1b1')
# ValueError: could not convert string to float: '1b1'
# >>>
# >>> float(' 0.2\n')
# 0.2

