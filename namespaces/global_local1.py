var = 10
year = 2024


def func():
    var = 'def'
    day = 30
    print(f'в локальном пространстве имён {var = }')
    print(f'в локальном пространстве имён {year = }')
    # year = 2025


func()

print(f'в глобальном пространстве имён {var = }')
try:
    print(day)
except NameError:
    print(f"в глобальном пространстве имён переменной 'day' не существует")


def func2():
    global var
    print(f'в локальном пространстве имён {var = }')
    var = 'def'


func2()
print(f'в глобальном пространстве имён {var = }')

