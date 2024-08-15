jogadores = list()
dados = {}
gols = []
aproveitamento = 0
while True:
    print('===' * 18)
    dados['nome'] = str(input('Nome do jogador: ')).strip().lower().title()
    jogos = int(input('Quantos jogos foram jogados? '))
    for c in range(1, jogos+1):
        gols.append(int(input(f'Quantos gols \033[1;34m{dados["nome"]}\033[m fez no \033[1;34m{c}ª jogo\033[m? ')))
        aproveitamento += gols[c-1]
    dados['gols'] = gols[:]
    dados['aproveitamento'] = aproveitamento
    jogadores.append(dados.copy())
    gols.clear()
    aproveitamento = 0
    while True:
        resp = str(input('Quer adicionar mais um jogador? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).strip()[0]
        if resp in 'SsNn':
            break
        print('\033[1;31mERRO!\033[m Por favor, digite apenas \033[1;32mS\033[m ou \033[1;31mN\033[m.')
    if resp in 'Nn':
        break
print('-=-' * 18)
print(f'\033[1m{'cod'} \033[1;34m{'NOME':<17}\033[1;35m{'GOLS':<18}\033[1;33m{'TOTAL'}\033[m')
print('===' * 18)
# for k, v enumerate(jogadores):
    # print(f'{k:>4} ', end='')
    # for d in v.values():
        # print(f'{str(d):<15}', end='')
    # print()
for a in range(0, len(jogadores)):
    print(f'\033[1m{a:^3} \033[1;34m{jogadores[a]["nome"]:<17}\033[1;35m{str(jogadores[a]["gols"]):<18}'
          f'\033[1;33m{jogadores[a]["aproveitamento"]}\033[m')
print('===' * 18)
while True:
    x = int(input('Mostrar dados de qual jogador? (\033[1;31m999 para parar\033[m) '))
    if x == 999:
        break
    elif len(jogadores) - 1 < x or x < 0:
        print(f'\033[1;31mERRO! Não existe jogador com código {x}!\033[m Tente novamente...')
    else:
        print(f'=> LEVANTANDO DO JOGADOR \033[1;34m{jogadores[x]["nome"]}\033[m:')
        for a, b in enumerate(jogadores[x]["gols"]):
            print(f'   -> No\033[1;34m jogo {a}\033[m fez \033[1;35m{b} gols\033[m.')
    print('===' * 18)
print('\033[1m<< VOLTE SEMPRE >>\033[m')
