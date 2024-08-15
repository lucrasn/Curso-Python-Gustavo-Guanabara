# # from random import sample
from random import randint
from time import sleep
print('='*41 + f'\n{'\033[1;34mJOGADA NA MEGA SENA\033[m':^49}\n' + '='*41)
a = int(input('Quantos jogos você quer que eu sorteie? '))
c = []
print('=' * 11 + f'\033[1;35m SORTEANDO {a} JOGOS \033[m' + '=' * 11)
# jogos = list()
# tot = 0
# while tot <= a:
for sorteio in range(1, a+1):
    # # c.append(sample(range(1, 7), 6))
    # # c[0].sort()
    # cont = 0
    # while True:
    while len(c) != 6:
        d = randint(1, 60)
        if d not in c:
            c.append(d)
            # cont += 1
        # if cont >= 6
            # break
    # c.sort()
    # jogos.append(c[:])
    # c.clear()
    # tot += 1
# for i, l in enumerate(jogos):
    # print(f'Jogo {i=1}: {l}')
    c.sort()
    print(f'Jogo \033[1;32m{sorteio}\033[m: \033[1;35m{c}\033[m')
    sleep(0.5)
    c.clear()
print('='*14 + ' \033[1;32m<BOA SORTE>\033[m ' + '='*14)
