a = float(input('Введите первое число: '))
b = float(input('Введите первое число: '))

zn = str(input('Введите операцию: '))

if zn == '+':
    print(a+b)
elif zn == '-':
    print(a-b)
elif zn == '*':
    print(a*b)
if zn == '/':
    if b!=0:
        print(a/b)
    else:
        print('На ноль делить нельзя')
else:
    print('Ненене, так не пойдет, друг')
