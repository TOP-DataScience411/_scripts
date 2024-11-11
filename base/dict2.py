# >>> {[1, 2]: 'abc'}
# TypeError: unhashable type: 'list'
# >>>
# >>> {{1, 2}: 'abc'}
# TypeError: unhashable type: 'set'
# >>>
# >>> {{1: 2}: 'abc'}
# TypeError: unhashable type: 'dict'

test_dict = {
                      1: 2.2, 
                    0.3: {5: 6}, 
                    '7': {8, 9}, 
               (10, 11): [12, 13, 14], 
              range(15): 16, 
    frozenset({17, 18}): '19'
}

# for key in test_dict.keys():
for key in test_dict:
    print(type(key), key, '', sep='\n')
print()

for value in test_dict.values():
    print(type(value), value, '', sep='\n')
print()

for item in test_dict.items():
    print(type(item), item, '', sep='\n')
print()

for key, value in test_dict.items():
    print(f'{key = }\n{value = }\n')
print()

