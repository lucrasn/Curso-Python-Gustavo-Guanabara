print('\033[1;35mCONTAGEM MÁGICA\033[m')
print('\033[1mSó números pares somam.\033[m')
print('-=-'*8)
soma = 0
for c in range(0, 6):
    numero = int(input(f'Digite o {c}º valor: '))
    if numero % 2 == 0:
        soma += numero
print(f'A soma dos número pares é \033[1;35m{soma}\033[m!')
