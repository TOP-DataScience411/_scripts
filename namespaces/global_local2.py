var = 10
year = 2024


def func(arg=None):
    var = 'def'
    day = 30
    print('\nглобальное пространство имён:', globals(), '', sep='\n')
    print('текущее пространство имён:', locals(), '', sep='\n')


print('\nглобальное пространство имён:', globals(), '', sep='\n')
print('текущее пространство имён:', locals(), '', sep='\n')

func()
func(0.001)

