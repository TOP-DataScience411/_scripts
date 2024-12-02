"""
module1.py — файл, содержащий основной управляющий код
путь к этому файлу передаётся интерпретатору в качестве аргумента
на основе этого файла создаётся модуль, который становится точкой входа
"""

print('начало выполнения кода модуля 1')

# print(__doc__, end='\n\n')


import module2

# >>> locals()
# {'__name__': '__main__', '__doc__': '\nmodule1.py — файл, содержащий основной управляющий код\nпуть к этому файлу передаётся интерпретатору в качестве аргумента\nна основе этого файла создаётся модуль, который становится точкой входа\n', '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000026B1C23B9E0>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'module2': <module 'module2' from 'D:\\G-Doc\\TOP Academy\\Data Science\\411\\scripts\\namespaces\\module2.py'>}
# >>>
# >>>
# >>> module2
# <module 'module2' from 'D:\\G-Doc\\TOP Academy\\Data Science\\411\\scripts\\namespaces\\module2.py'>
# >>>
# >>> type(module2)
# <class 'module'>
# >>>
# >>>
# >>> for var, obj in module2.__dict__.items():
# ...   if not var.startswith('_'):
# ...     print(f'{var!r}: {obj!r}')
# ...
# 'module3': <module 'module3' from 'D:\\G-Doc\\TOP Academy\\Data Science\\411\\scripts\\namespaces\\module3.py'>
# 'var1': 1368
# 'var2': 'lorem ipsum'
# >>>
# >>>
# >>> module2.var1
# 1368
# >>>
# >>> module2.var2
# 'lorem ipsum'
# >>>
# >>> module2.module3
# <module 'module3' from 'D:\\G-Doc\\TOP Academy\\Data Science\\411\\scripts\\namespaces\\module3.py'>
# >>>
# >>>
# >>> module2.module3.func1
# <function func1 at 0x0000026B1C673BA0>
# >>>
# >>> module2.module3.func1()
# вызов globals() из функции module3.func1()
# 'func1': <function func1 at 0x0000026B1C673BA0>


from module3 import func1

print(f'\n{module2.module3.func1 is func1 = }\n')

func1()


print('конец выполнения кода модуля 1')

# начало выполнения кода модуля 1
# начало выполнения кода модуля 2
# начало выполнения кода модуля 3
# конец выполнения кода модуля 3
# конец выполнения кода модуля 2
# 
# module2.module3.func1 is func1 = True
# 
# вызов globals() из функции module3.func1()
# 'func1': <function func1 at 0x000001F656313BA0>
# конец выполнения кода модуля 1

