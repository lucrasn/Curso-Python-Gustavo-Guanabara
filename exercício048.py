print('\033[1;33mSOMA DOS NÚMEROS ÍMPARES MÚLTIPLOS DE TRÊS DE 1 ATÉ 500\033[m')
print('-=-'*19)
soma = 0
cont = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        # acumulando
        soma += c
        # contando
        cont += 1
# for c in range(3, 500, 6):
    # n += c
print(f'A soma é dos \033[1;33m{cont}\033[m números solicitados é \033[1;33m{soma}\033[m')
