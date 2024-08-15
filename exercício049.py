from time import sleep
print('\033[1;35mTABUADA MÁGICA\033[m')
x = int(input('Digite um número: '))
print('\033[1mFAZENDO CALCULOS INIMAGINÁVEIS...\033[m')
sleep(1.5)
cor = {'verde': '\033[1;32m', 'amarelo': '\033[1;33m', 'azul': '\033[1;34m', 'limpo': '\033[m'}
for c in range(0, 11):
    print(f'{cor['verde']}{x}{cor['limpo']} \033[1mx {cor['amarelo']}{c:2}{cor['limpo']} '
          f'\033[1m= {cor['azul']}{x*c}{cor['limpo']}')
