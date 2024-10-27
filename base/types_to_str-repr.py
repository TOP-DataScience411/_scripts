from decimal import Decimal as dec

# repr — машиночитаемое строковое представление
# str — человекочитаемое строковое представление
print(str(1), repr(1), sep='\n', end='\n\n')
print(str(2.3), repr(2.3), sep='\n', end='\n\n')
print(str(dec('0.1')), repr(dec('0.1')), sep='\n', end='\n\n')
print(str('строка 1\nстрока 2'), repr('строка 1\nстрока 2'), sep='\n', end='\n\n')
print(str([1, 2.2, 'три']), repr([1, 2.2, 'три']), sep='\n', end='\n\n')
print(str({'3': 0.3, '5': 0.5}), repr({'3': 0.3, '5': 0.5}), sep='\n', end='\n\n')

