from random import randint
print('\033[1mVAMOS JOGAR \033[34mPAR\033[m \033[1mOU \033[33mÍMPAR\033[m')
print('-=-'*10)
x = 0
while True:
    comp = randint(0, 10)
    valor = int(input('Diga o valor: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou Ímpar? [\033[1;34mP\033[m/\033[1;33mI\033[m] ')).upper().strip()
    print('-=-'*10)
    soma = comp + valor
    # fez essa parada do é par e é ímpar depois do print do resultado ->
    if soma % 2 == 0:
        result = '\033[1;34mPAR\033[m'
    else:
        result = '\033[1;33mÍMPAR\033[m'
    # colocou end='' nesse print ->
    print(f'Você escolheu \033[1;35m{valor}\033[m e o computador \033[1;35m{comp}\033[m, '
          f'a soma deu \033[1;35m{soma}\033[m e esse número é {result}')
    # print('PAR' if result % 2 == 0 else 'ÍMPAR') -> ai como o print anterior tinha o end='' puxava o resultado
    if pi == 'P':
        if soma % 2 == 0:
            print('\033[1;32mPARABÉNS VOCÊ GANHOU!!\033[m')
            print('Vamos jogar novamente...')
            x += 1
        else:
            print('\033[1;31mVOCÊ PERDEU\033[m')
            print(f'Você\033[1;32m ganhou {x} vezes\033[m.')
            break
    if pi == 'I':
        if soma % 2 == 1:
            print('\033[1;32mPARABÉNS VOCÊ GANHOU!!\033[m')
            print('Vamos jogar novamente...')
            x += 1
        else:
            print('\033[1;31mVOCÊ PERDEU!!\033[m')
            print(f'Você\033[1;32m ganhou {x} vezes\033[m.')
            break
    print('-=-' * 10)
print('\033[1;35mOBRIGADO POR JOGAR!\033[m')
