def season(s):
    for i in season1:
        if s == i:
            print(season1[s])
season1 = {12: 'winter', 1: 'winter', 2: 'winter',
            3: 'spring', 4: 'spring', 5: 'spring',
           6: 'summer', 7: 'summer', 8: 'summer',
           9: 'autumn', 10: 'autumn', 11: 'autumn'}
s = int(input('Enter number:'))
season(s)
