lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('='*41 + f'\n\033[1;34m{'LISTAGEM DE PREÇOS':^40}\033[m\n' + '='*41)
# for c in range(0, len(lista)):
    # if c % 2 == 0:
        # print(f'{lista[c]:.<30}', end='')
    # else:
        # print(f'{lista[c]:>7.2f}')
a = 0
b = 1
while b != 19:
    print(f'\033[1;33m{lista[a]:.<32}\033[m\033[1;35mR${lista[b]:>7.2f}\033[m')
    a += 2
    b += 2
print('='*41)
