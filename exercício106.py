def ajuda():
    while True:
        print('\033[7;1;32;40m~' * 27)
        print(f'  SISTEMA DE AJUDA PyHELP')
        print('~' * 27)
        a = str(input('\033[mhelp > ')).strip()
        if a == 'fim':
            print('\033[7;1;31;40m~' * 13)
            print(f'  ATÉ LOGO!')
            print('~' * 13)
            break
        w = f'Acessando o manual do comando "{a}"'
        print('\033[7;1;34;40m~' * (len(w) + 4))
        print(f'  {w}')
        print('~' * (len(w) + 4))
        print('\033[7;1;33;40m', end='')
        print(f'{help(a)}')


ajuda()

# Guanabara
# from time import sleep
# c = ('\033[m', '\033[30;41m', '\033[30;42m', '\033[30;43m', '\033[30;44m', '\033[30;45m', '\033[7;30m')
# def ajuda(com):
    # título(f'Acessando o manual do comando \'{com}\'', 4)
    # print(c[6], end='')
    # help(com)
    # print(c[0], end='')
    # sleep(2)
# def título(msg, cor=0):
    # tam = len(msg) + 4
    # print(c[cor], end='')
    # print('~' * tam)
    # print(f'  {msg}')
    # print('~' * tam)
    # print(c[0] ,end='')
    # sleep(1)
# comando = ''
# while True:
    # título(''SISTEMA DE AJUDA PyHELP', 2)
    # comando = str(input('Função ou Biblioteca > '))
    # if comando.upper() == 'FIM':
        # break
    # else:
        # ajuda(comando)
# título('ATÊ LOGO!', 1)
