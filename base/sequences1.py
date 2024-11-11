furniture = [
    'кровать',
    'шкаф',
    'комод',
    'тумбочка',
    'тумбочка',
]

# >>> furniture.index('шкаф')
# 1
# >>> furniture.index('комод')
# 2
# >>> furniture.index('тумбочка')
# 3
# >>> furniture.index('тумба')
# ValueError: 'тумба' is not in list

# >>> furniture.count('комод')
# 1
# >>> furniture.count('тумбочка')
# 2
# >>> furniture.count('тумба')
# 0


shelves = furniture[2]

# >>> shelves.index('к')
# 0
# >>> shelves.index('о')
# 1
# >>> shelves.index('о', 2)
# 3
# >>> shelves[2:].index('о')
# 1

# >>> shelves.index('ко')
# 0
# >>> shelves.index('ом')
# 1
# >>> shelves.index('омо')
# 1
# >>> shelves.index('оно')
# ValueError: substring not found

