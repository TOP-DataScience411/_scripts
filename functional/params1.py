def adder(num1, num2):
    result = num1 + num2
    # print(f'{num1} + {num2} = {result}')
    return result


# >>> adder()
# TypeError: adder() missing 2 required positional arguments: 'num1' and 'num2'
# >>>
# >>> adder(5)
# TypeError: adder() missing 1 required positional argument: 'num2'
# >>>
# >>> adder(5, 10)
# 15


def multiplier(num1, num2):
    return num1 * num2

