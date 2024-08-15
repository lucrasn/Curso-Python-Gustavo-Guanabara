from time import sleep
# def maior(*x):
    # cont = maior = 0
    # print('Analisando os valores passados… ')
    # for valor in x:
        # print(f'{valor} ', end='', flush=True)
        # if cont == 0:
            # maior = valor
        # else:
            # if valor > maior:
                # maior = valor
        # cont += 1
    # print(f'Foram informados {cont} valores no total.')
    # print(f'O maior valor informado foi {maior}.')
# def maior(x):


def maior(*x):
    print('-=' * 18)
    print('\033[1;33mAnalisando os valores passados...\033[m')
    for y in x:
        print(y, end=' ')
        sleep(0.5)
    print(f'Foram informados \033[1;34m{len(x)} valores\033[m ao todo.')
    sleep(1)
    if x != ():
        print(f'O \033[1;31mmaior valor\033[m informado foi \033[1;31m{max(x)}\033[m.')
    else:
        print('O \033[1;31mmaior valor\033[m informado foi \033[1;31m0\033[m.')


# lista = []
# while True:
    # lista.append(int(input('Digite um número inteiro: ')))
    # while True:
        # resp = str(input('Quer adicionar mais um número: [S/N] ')).strip().upper()[0]
        # if resp in 'SN':
            # break
        # print('ERRO! Por favor, responda somente S ou N.')
    # if resp == 'N':
        # break
# maior(lista)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
