#!/usr/bin/python3
#from sys import argv
from datetime import date
from locale import LC_ALL, setlocale
from re import match
from calendar import day_abbr, monthcalendar

setlocale(LC_ALL, '')

def is_now (_day, _today, _color, _default):
    _pattern = '^[123 ][0-9]$'
    if match(_pattern, _day):
        if int(_day) == _today:
            return f'{_color}{_day}{_default}'
        else:
            return _day
    else:
        return _day

def weeks_to_str (no_day, _month):
    for i, week in enumerate(_month):
        _month[i] = [int_to_str(day, no_day) for day in week]
    return _month

int_to_str = lambda d, nd: str(d) if d > 9 else f' {d}' if d > 0 else nd

days_name = [d[:2].title() for d in list(day_abbr)]
now = date.today()
year_month = tuple([int(x) for x in now.strftime('%Y-%m').split('-')])
today = int(now.strftime('%d'))
month = monthcalendar(*year_month)

if __name__ == '__main__':
    month = weeks_to_str('  ', month)
    for i, w in enumerate(month):
        month[i] = [is_now(d, today, '\033[1m', '\033[0m') for d in month[i]]
    month.insert(0, days_name)
    for i, w in enumerate(month):
        if i == 0:
            print (f'\033[1m{"  ".join(w)}\033[0m')
        else:
            print ('  '.join(w))
