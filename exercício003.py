x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
soma = x + y
# print('A soma entre {} e {} é {}!'.format(x, y, soma))
print(f'A soma entre \033[1;33m{x}\033[m e \033[1;34m{y}\033[m é \033[1;35m{soma}\033[m!')
