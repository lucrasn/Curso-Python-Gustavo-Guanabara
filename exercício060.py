print('\033[1;34mNÚMERO \033[33mFATORIAL\033[m\033[1m:\033[m')

# primeira forma de fazer:
# from math import factorial
# x = int(input('Digite um número: '))
# print(f'O número \033[1;34m{x}\033[m em fatorial é \033[1;33m{factorial(x)}\033[m')

# segunda forma de fazer:
# x = int(input('Digite um número: '))
# fac = 1
# num = ''
# if x == 1:
    # print(f'\033[1;34m{x}!\033[m =', end='')
# for c in range(x, 1, -1):
    # fac *= c
    # if x > 1:
        # if c == x:
            # print(f'\033[1;34m{x}!\033[m =', end='')
        # print(f' {c} x', end='')
# print(f' 1 = \033[1;33m{fac}\033[m')

# terceira forma de fazer:
x = int(input('Digite um número: '))
fac = 1
y = x
while y != 0:
    if y == x:
        print(f'\033[1;34m{x}!\033[m = ', end='')
    print(f'{y}', end='')
    # if y != 1:
        # print(f' {y} x', end='')
    fac *= y
    y -= 1
    print(' x ' if y != 0 else ' = ', end='')
# print(f' 1 = \033[1;33m{fac}\033[m')
print(f'\033[1;33m{fac}\033[m')
