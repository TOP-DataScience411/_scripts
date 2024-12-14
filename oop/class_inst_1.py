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

