from time import sleep
from random import choice
# from random import randint
print('\033[1;32mJOGO DO JOKENPÔ\033[m')
win = 0
while not win == 3:
    print('-=-' * 6)
    # escolhendo a jogada do jogador
    A = str(input('\033[1;33mPedra\033[m,\033[1;34m papel\033[m e\033[1;35m tesoura\033[m: ')).strip().upper()
    # escolhendo a jogada do computador
    B = choice(['PEDRA', 'PAPEL', 'TESOURA'])
    b = B.lower()
    # itens = ('PEDRA', 'PAPEL', 'TESOURA')
    # B = itens[randint(0, 2)]
    print('-=-'*6)
    # dando uma pause de 3 segundos
    sleep(1)
    print('\033[1mJO\033[m')
    sleep(1)
    print('\033[1mKEN\033[m')
    sleep(1)
    print('\033[1mPÔ!!!\033[m')
    # condições para ganhar e perder
    if A == B:
        print('\033[1;36mEMPATE\033[m', end='')
        print(f', eu joguei {b} também.')
    elif A == 'PEDRA':
        if B == 'TESOURA':
            print(f'\033[1;32mVITORIA!!!\033[m eu perdi completamente, joguei \033[1;35m{b}\033[m.')
            win += 1
        else:
            print(f'\033[1;31mDERROTA!!!\033[m hahaha não foi sua jogada da sorte, eu joguei \033[1;34m{b}\033[m.')
            win -= 1
    elif A == 'PAPEL':
        if B == 'PEDRA':
            print(f'\033[1;32mVITORIA!!!\033[m eu perdi completamente, joguei \033[1;33m{b}\033[m.')
            win += 1
        else:
            print(f'\033[1;31mDERROTA!!!\033[m hahaha não foi sua jogada da sorte, eu joguei \033[1;35m{b}\033[m.')
            win -= 1
    elif A == 'TESOURA':
        if B == 'PAPEL':
            print(f'\033[1;32mVITORIA!!!\033[m eu perdi completamente, joguei \033[1;34m{b}\033[m.')
            win += 1
        else:
            print(f'\033[1;31mDERROTA!!!\033[m hahaha não foi sua jogada da sorte, eu joguei \033[1;33m{b}\033[m.')
            win -= 1
    # se a pessoa digitar nada com nada.
    else:
        print('Procure digitar corretamento\033[1;33m pedra\033[m,\033[1;34m papel\033[m ou\033[1;35m tesoura\033[m.')
