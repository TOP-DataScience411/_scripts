# внешние пакеты
from psycopg import connect
# стандартная библиотека
from json import loads as json_loads
from pprint import pprint
from pathlib import Path
from sys import path
# текущий проект
import queries


config_path = Path(path[0]) / 'config.json'
config = json_loads(config_path.read_text())

connection = connect(**config, autocommit=True)

with connection.cursor() as cursor:
    cursor.execute(queries.sel_donations_by_year)
    donations_by_year = cursor.fetchall()
    
    count_week_vacations = cursor.execute(queries.sel_count_week_vacations).fetchall()
    
    groupconcat_wards_departments = cursor.execute(queries.sel_groupconcat_wards_departments)\
                                          .fetchall()
    
    large_donations = cursor.execute(queries.sel_large_donations).fetchall()


# >>> print(*donations_by_year, sep='\n')
# (Decimal('2014'), Decimal('2727295.65'))
# (Decimal('2015'), Decimal('862164.14'))
# (Decimal('2016'), Decimal('345820.65'))
# (Decimal('2017'), Decimal('3298987.09'))
# (Decimal('2018'), Decimal('2433153.55'))
# (Decimal('2019'), Decimal('2046515.83'))
# (Decimal('2020'), Decimal('1527585.77'))
# (Decimal('2021'), Decimal('1402189.73'))
# (Decimal('2022'), Decimal('1764004.33'))
# (Decimal('2023'), Decimal('2540430.87'))
# (Decimal('2024'), Decimal('295151.37'))


# >>> print(*count_week_vacations, sep='\n')
# ('неделя', 54)
# ('больше недели', 196)

