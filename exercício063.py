print('\033[1;36mSEQUÊNCIA DE FIBONACCI\033[m')
fibonacci = int(input('Digite a quantidade de termos da Sequência de Fibonacci que você quer ver: '))
print('-=-'*24)
termos = 0
a = 0
b = 1
c = 0
if fibonacci != 1:
    print(f'Esses são os \033[1;36m{fibonacci}\033[m primeiros termos da Sequência de Fibonacci:')
if fibonacci == 1:
    print(f'Esse é o \033[1;36m{fibonacci}º\033[m termo da Sequencia de Fibonacci.')
while termos != fibonacci:
    if termos > 2:
        a = b
        b = c
        c = a + b
    if termos < fibonacci-1:
        print(f'\033[1;36m{c}\033[m -> ', end='')
    if termos == fibonacci-1:
        print(f'\033[1;36m{c}\033[m')
    c = a + b
    termos += 1
