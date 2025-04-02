#!/usr/bin/python3
from sys import argv, exit
from cal import days_name, is_now, month, now, today, weeks_to_str

if len(argv) == 1 or len(argv) > 4:
    exit(1)

params = argv[1:]
spaces = 0

if len(params) == 1 and params[0] == 'month':
    print (now.strftime('%B %Y').title())
    exit(0)

if params[-1].isdecimal():
    spaces = int(params[-1])
    params = params[:-1]

if len(params) == 1:
    names = mark = params[0]
else:
    names, mark = params

month = weeks_to_str('--', month)

while len(month) < 6:
    month.append(['--'] * 7)

for i, w in enumerate(month):
    month[i] = [is_now(d, today, mark, '$color') for d in month[i]]
month.insert(0, days_name)
print (now.strftime('%B %Y').title() + ' $hr$color')
for i, w in enumerate(month):
    if i == 0:
        print (f'$alignc{names}{"  ".join(w)}$color')
    else:
            print ('${alignc}' + '  '.join(w))
