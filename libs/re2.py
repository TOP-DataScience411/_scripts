from pathlib import Path
from re import compile, MULTILINE
from sys import path


text = (Path(path[0]) / 'history_dates.txt').read_text('utf-8')

months = (
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря',
)

pat_date_DMY = compile(
    r'^(?P<day>[1-9]|(?:[12]\d|3[01])) '
    f"(?P<month>{'|'.join(months)}) "
    r'(?P<year>1[89]\d\d|20[012]\d) г\.',
    MULTILINE
)
dates = list(pat_date_DMY.finditer(text))

# >>> mo = dates[0]
# >>>
# >>> mo.group()
# '20 ноября 1805 г.'
# >>>
# >>> mo.group() == mo.group(0) == mo[0]
# True
# >>>
# >>> mo.group(1)
# '20'
# >>> mo.group(2)
# 'ноября'
# >>> mo.group(3)
# '1805'
# >>>
# >>> mo.group(1) == mo.group('day') == mo[1] == mo['day']
# True
# >>> mo.group(2) == mo.group('month') == mo[2] == mo['month']
# True
# >>> mo.group(3) == mo.group('year') == mo[3] == mo['year']
# True

