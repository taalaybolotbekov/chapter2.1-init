def is_year_leap(s):
    if s % 4 == 0:
        print('високосный год')
    else:
        print('невисикосоный год')
s = int(input(': '))
is_year_leap(s)