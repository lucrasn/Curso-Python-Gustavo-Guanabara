from time import sleep
print('\033[1mCALCULADORA ALTERNATIVA\033[m')
lista = []
x = 0
for c in range(1, 3):
    a = int(input(f'Digite o {c}º número: '))
    lista += [a]
while x != 5:
    print('-=-'*10)
    print('\033[1mMENU DE ESCOLHA:\033[m')
    print('''\033[1;35m[ 1 ] somar\033[m
\033[1;33m[ 2 ] multiplicar\033[m
\033[1;34m[ 3 ] maior\033[m
\033[1;32m[ 4 ] novos números\033[m
\033[1;31m[ 5 ] sair do programa\033[m''')
    x = int(input('Digite o número correspondente com a ação: '))
    print('-=-' * 10)
    if x == 1:
        print(f'\033[1;35m{lista[0]} + {lista[1]} = {lista[0] + lista[1]}\033[m')
    elif x == 2:
        print(f'\033[1;33m{lista[0]} x {lista[1]} = {lista[0] * lista[1]}\033[1;35m')
    elif x == 3:
        if lista[0] > lista[1]:
            print(f'\033[1;34mO maior valor é {lista[0]}\033[m.')
        elif lista[0] == lista[1]:
            print('\033[1;34mO dois valores são iguais\033[m.')
        else:
            print(f'\033[1;34mO maior valor é {lista[1]}\033[1;34m.')
    elif x == 4:
        lista = []
        for c in range(1, 3):
            a = int(input(f'Digite o {c}º número: '))
            lista += [a]
    elif x < 1 or x > 5:
        print('\033[1mOpção inválida. Tente novamente.\033[m')
    sleep(1.5)
print('\033[1mFINALIZANDO...\033[m')
sleep(1.5)
print('\033[1;31mOBRIGADO POR ÚTILIZAR O MEU PROGRAMA!\033[m')
