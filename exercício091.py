from random import randint
from time import sleep
from operator import itemgetter
sorteio = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
print('Valores sorteados:')
sleep(0.2)
for k, v in sorteio.items():
    print(f'    O \033[1;34m{k}\033[m tirou \033[1;35m{v}\033[m')
    sleep(0.8)
print('-=-' * 15)
print('Ranking dos jogadores: ')
sleep(0.2)
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    \033[1;33m{i+1}ª lugar\033[m: \033[1;34m{v[0]}\033[m com \033[1;35m{v[1]}\033[m')
    sleep(0.8)
