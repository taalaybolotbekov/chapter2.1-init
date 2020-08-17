name = {'Усейн Болт': '1', 'Taalay': '2', 'Aibek': '3'}
place = {'1': 'UB', '2': 'Taalay', '3': 'Aibek'}
def get_key(value):
    print(name[value])
def get_value(key):
    print(place[key])

get_key(input('Name: '))

get_value(input('Place: '))