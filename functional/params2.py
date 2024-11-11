def calculator(num1, num2, operation='+'):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2


# >>> calculator(1, 5)
# 6
# >>> calculator(1, 5, '-')
# -4
# >>> calculator(1, 5, '*')
# 5
# >>> calculator(1, 5, '/')
# 0.2


# def test_func1(param1=10, param2):
#     pass

# SyntaxError: parameter without a default follows parameter with a default


# def test_func2(par1, par2=10, par3):
#     pass

# SyntaxError: parameter without a default follows parameter with a default


# >>> calculator(num1=12, num2=12, operation='*')
# 144
# >>>
# >>> calculator(num1=12, operation='+', num2=12)
# 24
# >>>
# >>> calculator(operation='-', num2=12, num1=25)
# 13


# >>> calculator(17, 14, operation='*')
# 238
# >>>
# >>> calculator(15, operation='*', 15)
# SyntaxError: positional argument follows keyword argument

