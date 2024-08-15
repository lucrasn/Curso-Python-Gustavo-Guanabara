print('\033[1;34mPROGRESSÃO ARITMÉTICA:\033[m')
a1 = int(input('Primeiro termo da progressão: '))
r = int(input('Razão da progressão: '))
print('\033[1;34mOs 10 primeiros termos dessa PA são:\033[m')
print('P.A (', end='')
# decimo = a1 + (10 - 1) * r
# for c in range(a1, decimo + r, r):
for c in range(0, 10):
    # an = a1 + (r * c)
    if c < 9:
        print(f'{a1}, ', end='')
    else:
        print(f'{a1}...)')
    a1 += r
