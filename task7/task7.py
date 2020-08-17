def arithmetic(x,y,z):
    if z == '+':
        print(x+y)
    elif z == '/':
        print(x/y)
    elif z == '-':
        print(x-y)
    elif z == '*':
        print(x*y)
    else:
        print('Не буду делать')
x = int(input('введите первое числр: '))
y = int(input('введите второе число: '))
z = input('введите оператор: ')
arithmetic(x,y,z)