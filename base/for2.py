items = [1, 2.2, 'три', [4, '5'], (6, 7.7, 0.8)]

generator = enumerate(items)
for i, items_elem in generator:
    print(f'{i = }\t{items_elem}')

# >>> generator
# <enumerate object at 0x00000143697ED6C0>
# >>> 
# >>> type(generator)
# <class 'enumerate'>


# i = 0   1
# i = 1   2.2
# i = 2   три
# i = 3   [4, '5']
# i = 4   (6, 7.7, 0.8)

