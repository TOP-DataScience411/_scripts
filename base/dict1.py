people_age = {'Иван': 35, 'Артём': 41, 'Анна': 32, 'Лиза': 17}

# >>> type(people_age)
# <class 'dict'>
# >>>
# >>> len(people_age)
# 4
# >>>
# >>> people_age['Иван']
# 35
# >>> people_age['Анна']
# 32
# >>>
# >>> people_age['Олеся']
# KeyError: 'Олеся'
# >>>
# >>> people_age.get('Лиза')
# 17
# >>> people_age.get('Олеся')
# >>>
# >>>
# >>> people_age.get('Лиза', 0)
# 17
# >>> people_age.get('Олеся', 0)
# 0


for name, age in people_age.items():
    if age == 17:
        print(name)

# Лиза
# >>>


# >>> people_age['Артём'] = 42
# >>> people_age['Артём']
# 42
# >>>
# >>> id(people_age)
# 2935017812928
# >>>
# >>> people_age['Лиза'] += 1
# >>> people_age
# {'Иван': 35, 'Артём': 42, 'Анна': 32, 'Лиза': 18}
# >>>
# >>> id(people_age)
# 2935017812928


