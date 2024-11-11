def get_name():
    while True:
        name = input('\nвведите имя: ')
        if name.isalpha():
            return name
        print('! имя должно содержать только буквенные символы !')


# >>> get_name()
# 
# введите имя: Геннадий Дмитриевич
# ! имя должно содержать только буквенные символы !
# 
# введите имя: GennDALF123
# ! имя должно содержать только буквенные символы !
# 
# введите имя: Геннадий
# 'Геннадий'
# >>>
# >>> name = get_name()
# 
# введите имя: Геннадий
# >>>
# >>> name
# 'Геннадий'
# >>>


def ascii_geometry():
    command = input('\nвведите название фигуры: ')
    
    if command == 'отрезок':
        return '—'*50
    
    elif command == 'квадрат':
        result = '—'*50 + '\n'
        for _ in range(5):
            result += '|' + ' '*48 + '|\n'
        result += '—'*50
        return result
    
    elif command == 'круг':
        print('! не могу рисовать круги =( !')
    
    else:
        print('! неизвестная фигура !')
    
    return ''


figures = []
for _ in range(4):
    figures.append(ascii_geometry())

# >>> len(figures)
# 4

for fig in figures:
    print(repr(fig))

# '——————————————————————————————————————————————————'
# '——————————————————————————————————————————————————'
# ''
# '——————————————————————————————————————————————————'

