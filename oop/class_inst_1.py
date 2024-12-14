class Table:
    def __init__(self, legs_number, table_height, table_length, table_width):
        self.legs = legs_number
        self.height = table_height
        self.length = table_length
        self.width = table_width
        self.objects = []
    
    def put_on_table(self, *objects):
        self.objects.extend(objects)

# объект класса
# >>> Table
# <class '__main__.Table'>


# создание экземпляров
computer_table = Table(6, 650, 1550, 800)
dinner_table = Table(4, 860, 1200, 1200)

# экземпляры класса
# >>> computer_table
# <__main__.Table object at 0x0000019DD9834950>
# >>>
# >>> dinner_table
# <__main__.Table object at 0x0000019DD9834980>


# >>> type(computer_table) is computer_table.__class__ is Table
# True


# обращения к атрибутам
print(
    computer_table.legs,
    dinner_table.legs
)
# 6 4

# вызов методов
computer_table.put_on_table('keyboard', 'mouse')
dinner_table.put_on_table('dishes')

print(*computer_table.objects)
print(*dinner_table.objects)
# keyboard mouse
# dishes


# внутреннее пространство имён экземпляра
# >>> computer_table.__dict__
# {'legs': 6, 'height': 650, 'length': 1550, 'width': 800, 'objects': ['keyboard', 'mouse']}

# внутреннее пространство имён объекта класса
# >>> Table.__dict__
# mappingproxy({'__module__': '__main__', '__init__': <function Table.__init__ at 0x0000019DD98339C0>, 'put_on_table': <function Table.put_on_table at 0x0000019DD9833A60>, '__dict__': <attribute '__dict__' of 'Table' objects>, '__weakref__': <attribute '__weakref__' of 'Table' objects>, '__doc__': None})

# полностью расширенная область видимости экземпляра
# >>> dir(computer_table)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'height', 'legs', 'length', 'objects', 'put_on_table', 'width']

