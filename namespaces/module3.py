"""
module2.py — файл, содержащий вспомогательные функции
на основе этого файла может быть создан модуль с помощью системы импорта
"""

print('начало выполнения кода модуля 3')


def func1():
    print('вызов globals() из функции module3.func1()')
    for var, obj in globals().items():
        if not var.startswith('_'):
            print(f'{var!r}: {obj!r}')


print('конец выполнения кода модуля 3')
