from datetime import (
    datetime as dt, 
    timedelta as td,
)

class_start = dt(2024, 12, 1, 15, 15)
current = dt.now()

# >>> class_start
# datetime.datetime(2024, 12, 1, 15, 15)
# >>>
# >>> current
# datetime.datetime(2024, 12, 1, 15, 48, 47, 54608)

interval = current - class_start

# >>> interval
# datetime.timedelta(seconds=2027, microseconds=54608)


print(class_start.strftime('%H:%M:%S — %d.%m.%Y'))
print(current.strftime('%H:%M:%S — %d.%m.%Y'))

# 15:15:00 — 01.12.2024
# 15:48:47 — 01.12.2024


from locale import LC_ALL, setlocale

setlocale(LC_ALL, 'ru_RU')

print(f'{current:%H:%M %d %B %Y}')

# 15:48 01 Декабрь 2024



# >>> dt.strptime('15.05.2009', '%d.%m.%Y')
# datetime.datetime(2009, 5, 15, 0, 0)
# >>>
# >>> dt.strptime('15.05', '%d.%m')
# datetime.datetime(1900, 5, 15, 0, 0)

