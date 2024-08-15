dados = {}
gols = []
aproveitamento = 0
dados['nome'] = str(input('Nome do jogador: ')).strip().lower().title()
jogos = int(input('Quantos jogos foram jogados? '))
for c in range(1, jogos+1):
    gols.append(int(input(f'Quantos gols {dados["nome"]} fez no {c}ª jogo? ')))
    aproveitamento += gols[c-1]
dados['gols'] = gols[:]
# dados['aproveitamento'] = sum(partidas)
dados['aproveitamento'] = aproveitamento
print('-=-' * 25)
print(dados)
print('-=-' * 25)
for k, v in dados.items():
    print(f'O campo \033[1;34m{k}\033[m tem o valor \033[1;35m{v}\033[m')
print('-=-' * 25)
# print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
print(f'\033[1;33mO jogador {dados["nome"]} jogou {jogos} partidas\033[m.')
for a, b in enumerate(dados["gols"]):
    print(f'    => \033[1;32mNa partida {a+1}\033[m, fez \033[1;31m{b} gols\033[m.')
print(f'\033[1;33mFoi um total de {dados["aproveitamento"]} gols\033[m.')
