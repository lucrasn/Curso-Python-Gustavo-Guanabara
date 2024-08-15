from random import randint
from time import sleep
lista = []


def sorteio(x):
    print('Sorteando \033[1;33m5 valores\033[m da lista: ', end='')
    for w in range(0, 5):
        # n = randint(1, 10)
        # lista.append(n)
        lista.append(randint(1, 10))
        # print(f'{n} ', end='', flush=True)
    for w in lista:
        print(f'\033[1m{w}\033[m', end=' ')
        sleep(1)
    print('\033[1;32mPRONTO!\033[m')
    sleep(1)


def soma_par(y):
    soma = 0
    for w in y:
        if w % 2 == 0:
            soma += w
    print(f'\033[1;34mSomando\033[m os valores \033[1;34mpares\033[m de {lista}, temos \033[1;34m{soma}\033[m')


sorteio(lista)
soma_par(lista)
