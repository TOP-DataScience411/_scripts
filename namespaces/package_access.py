import package

# >>> package
# <module 'package' from 'D:\\G-Doc\\TOP Academy\\Data Science\\411\\scripts\\namespaces\\package\\__init__.py'>


from pprint import pprint

pprint(
    {var: obj for var, obj in package.__dict__.items() if not var.startswith('_')}, 
    sort_dicts=False
)

# {'sub_package_1': <module 'package.sub_package_1' from 'D:\\G-Doc\\TOP Academy\\Data Science\\411\\scripts\\namespaces\\package\\sub_package_1\\__init__.py'>,
#  'var1': 2024,
#  'var2': 'Год Семьи',
#  'sub_package_2': <module 'package.sub_package_2' from 'D:\\G-Doc\\TOP Academy\\Data Science\\411\\scripts\\namespaces\\package\\sub_package_2\\__init__.py'>,
#  'today': datetime.date(2024, 11, 30)}


