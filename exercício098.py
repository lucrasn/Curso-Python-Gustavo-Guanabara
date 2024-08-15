from time import sleep
# def contador(i, f, p):
    # if p < 0:
        # p *= -1
    # if p == 0:
        # p = 1
    # print('-=' * 20)
    # print(f'Contagem de {i} até {f} de {p} em {p}')
    # sleep(2.5)
    # if i < f:
        # cont = i
        # while cont <= f:
            # print(f'{cont} ', end='', flush=True)
            # sleep(0.5)
            # cont += p
        # print('FIM')
    # else:
        # cont = i
        # while cont >= f:
            # print(f'{cont} ', end='', flush=True)
            # sleep(0.5)
            # cont -= p
        # print('FIM')


def contador(i, f, p):
    print('-=' * 20)
    if (i > f and p < 0) or (i < f and p < 0):
        p *= -1
    elif p == 0:
        p = 1
    print(f'Contagem de \033[1;34m{i}\033[m ate \033[1;33m{f}\033[m de \033[1;35m{p}\033[m em \033[1;35m{p}\033[m')
    sleep(2.5)
    if f > i:
        f += 1
    elif i > f and p > 0:
        p *= -1
        f -= 1
    for x in range(i, f, p):
        print(f'\033[1m{x}\033[m', end=' ')
        sleep(0.5)
    print('\033[1;31mFIM!\033[m')


contador(1, 10, 1)
contador(10, 0, -2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
contador(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))
