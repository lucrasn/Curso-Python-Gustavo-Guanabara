print('\033[1;33mTABUADA SUPREMA\033[m')
print('\033[1;31mDIGITE QUALQUER NÚMERO NEGATIVO PARA SAIR\033[m')
print('-=-'*14)
while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    # Guanabara não usou esse if ao inves disso ele so colocou um if num < 1: break
    if num >= 0:
        for tabuada in range(1, 11):
            print(f'\033[1;34m{num}\033[m x \033[1;32m{tabuada}\033[m = \033[1;35m{num*tabuada}\033[m')
    elif num < 0:
        break
    print('-=-'*14)
print('\033[1;33mTABUADA SUPREMA ENCERRADA\033[m. Volte sempre!')
