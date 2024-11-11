# for переменная_цикла in итерируемый_объект:
#     блок_тела_цикла
#     ...

items = [1, 2.2, 'три', [4, '5'], (6, 7.7, 0.8)]

for element in items:
    print(element, type(element), sep='\n', end='\n\n')

# 1
# <class 'int'>
# 
# 2.2
# <class 'float'>
# 
# три
# <class 'str'>
# 
# [4, '5']
# <class 'list'>
# 
# (6, 7.7, 0.8)
# <class 'tuple'>


items_len = len(items)
# i, j, k — традиционные имена переменных для индексов
for i in range(items_len):
    print(f'{i = }\t{items[i]}')

# i = 0   1
# i = 1   2.2
# i = 2   три
# i = 3   [4, '5']
# i = 4   (6, 7.7, 0.8)

