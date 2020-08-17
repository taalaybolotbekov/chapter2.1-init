A = 'ABCDEFGHIKLMNOPQRSTVWXYZ'
a = 'abcdefghiklmnopqrstvwxyz'

def spisok(x):
    a1 = 0
    b = 0
    for i in x:
        if i in A:
            a1+=1
        elif i in a:
            b+=1
    return('Большие: ', a1, 'маленькие: ', b)
print(spisok(input(': ')))


# ad = 'abcdefghijklmnopqrstuvwxyz'
# au = ad.upper()
# def a(s):
#     c = 0
#     v = 0
#     for i in s:
#         if i in ad:
#             c+=1
#         elif i in au:
#             v+=1
#     return [c,v]
#
# print(a(input()))