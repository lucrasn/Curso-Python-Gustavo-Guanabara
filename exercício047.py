from time import sleep
print('\033[1;34mNÚMERO PARES\033[m')
print('\033[1m-=\033[m'*7)
cor = {'azul': '\033[1;34m', 'limpar': '\033[m'}
for c in range(2, 51, 2):
    print(f'{cor['azul']}{c}{cor['limpar']}')
    sleep(0.5)
print('\033[1m-=\033[m'*7)
