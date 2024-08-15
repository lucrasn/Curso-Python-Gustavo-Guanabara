print('\033[1;35mPROGRESSÃO ARITMÉTICA 3.0:\033[m')
a1 = int(input('Primeiro termo da progressão: '))
r = int(input('Razão da progressão: '))
print('\033[1;35mOs 10 primeiros termos dessa PA são:\033[m')
print('\033[mP.A\033[m (', end='')
loop = 0
x = 0
while loop != 10:
    if loop < 9:
        print(f'{a1}, ', end='')
    else:
        print(f'{a1}...)')
    loop += 1
    a1 += r
    x += 1
cont = ''
while cont != 'N':
    print('\033[1m-=-\033[m'*18)
    cont = str(input('Você quer ver mais termos dessa \033[1;35mP.A\033[m '
                     '[\033[1;32mS\033[m/\033[1;31mN\033[m]? ')).upper().strip()
    termos = 0
    if cont == 'S':
        termos = int(input('Quantos\033[1;35m termos a mais\033[m você quer ver? '))
        print('\033[1;35mP.A\033[m (...', end='')
        for b in range(0, termos):
            if b < termos-1:
                print(f'{a1}, ', end='')
            else:
                print(f'{a1}...)')
            a1 += r
            x += 1
    elif cont != 'S' and cont != 'N':
        print('\033[1;31mDigite uma resposta válida!\033[m')
print(f'Progressão finalizada com \033[1;34m{x} termos mostrados\033[m.')
print('\033[1;35mOBRIGADO POR USAR MEU PROGRAMA!\033[m')

# professor Guanabara:
'''print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.'''
