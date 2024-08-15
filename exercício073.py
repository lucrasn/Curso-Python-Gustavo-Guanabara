brasileirao = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense', 'Athletico-PR',
               'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco', 'Bahia',
               'Santos', 'Goiás', 'Coritiba', 'América-MG')
print(f'Os\033[1;34m primeiros 5\033[m colocados são: {brasileirao[:5]}')
# print(f'Os últimos 4 colocados são: {brasileirao[-4:]}')
print(f'Os \033[1;33múltimos 4 colocados\33[m são: {brasileirao[16:]}')
print(f'Essa é a lista em \033[1;35mordem alfabética\033[m: {sorted(brasileirao)}')
print(f'O time \033[1;31mFlamengo\033[m está em \033[1;31m{brasileirao.index('Flamengo') + 1}ª lugar\033[m.')
