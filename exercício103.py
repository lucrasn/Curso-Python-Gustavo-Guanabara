def ficha(n='', g=''):
    """
    -> Mostra quantos gols o jogador fez em um campeonato
    :param n: Str do nome do jogador
    :param g: Int do número de gols
    :return: Sem retorno
    """
    if n == '' or n.isnumeric() or n.isspace():
        n = '\033[1;31m<desconhecido>\033[m'
    if g == '' or g.isalpha() or g.isspace():
        g = 0
    print(f'O jogador \033[1;35m{n}\033[m fez \033[1;34m{g}\033[m gol(s) no campeonato.')


print('-=' * 15)
ficha(str(input('Nome do jogador: ')),
      input('Número de gols: '))

# Guanabara
# def ficha(jog='<desconhecido>', gol=0):
    # print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')
    #
    #
# n = str(input('Nome do Jogador: '))
# g = str(input('Número de Gols: '))
# if g.isnumeric():
    # g = int(g)
# else:
    # g = 0
# if n.strip() == '':
    # ficha(gol=g)
# else:
    # ficha(n, g)
