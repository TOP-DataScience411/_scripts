# import cycled1
# print(cycled1.var)
# var = 200

# приведёт к: 
# AttributeError: partially initialized module 'cycled2' has no attribute 'var' (most likely due to a circular import)


import cycled_data
# механизм отложенного импорта приведёт к повторному выполнению кода модуля cycled1
# import cycled1

print(cycled_data.var1)

