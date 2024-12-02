# import cycled2
# var = 'просто переменная'
# print(cycled2.var)

# приведёт к: 
# AttributeError: partially initialized module 'cycled2' has no attribute 'var' (most likely due to a circular import)


import cycled_data
import cycled2

print(cycled_data.var2)

