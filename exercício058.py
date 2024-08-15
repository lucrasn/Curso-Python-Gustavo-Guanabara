from random import randint
print('Pesei num número de \033[1;34m0\033[m a \033[1;33m10\033[m tente adivinhar!')
y = -1
# acertou = False
palpite = 0
x = randint(0, 10)
# while not acertou:
while y != x:
    y = int(input('Em que número pensei? '))
    # if y == x:
        # acertou = True
    if x != y:
        if y > x:
            print('\033[1;34mMENOS... TENTE NOVAMENTE\033[m')
        else:
            print('\033[1;33mMAIS... TENTE NOVAMENTE\033[m')
    print('-=-'*9)
    palpite += 1
print(f'\033[1;32mPARABÉNS, VOCÊ VENCEU\033[m')
print(f'Foram necessárias \033[1;35m{palpite} tentativas para vencer\033[m.')
