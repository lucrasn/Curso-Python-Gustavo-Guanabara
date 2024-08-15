print('\033[1;33mPROGRESSÃO ARITMÉTICA 2.0:\033[m')
a1 = int(input('Primeiro termo da progressão: '))
r = int(input('Razão da progressão: '))
print('\033[1;33mOs 10 primeiros termos dessa PA são:\033[m')
print('P.A (', end='')
c = 0
while c != 10:
    # print(f'{a1}', end='')
    # print(', ' if c < 9 else ', ...)', end='')
    if c < 9:
        print(f'{a1}, ', end='')
    else:
        print(f'{a1}...)')
    c += 1
    a1 += r
# print('')
