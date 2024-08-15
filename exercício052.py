print('\033[1;34mPRIMO?\033[m')
print('-='*13)
x = int(input('Digite um número inteiro: '))
# tot = 0
# for c in range(1, x + 1):
    # if x % c == 0:
        # tot += 1
primo = '\033[1;34mÉ PRIMO\033[m'
for c in range(1, x):
    y = x % c
    if y == 0:
        if 1 < c:
            primo = '\033[1;31mNÃO É PRIMO\033[m'
# if tot > 2:
    # primo = 'NÃO É PRIMO'
if x == 1:
    print('O número 1 é engraçado ele \033[1;33mNÃO É PRIMO NEM COMPOSTO\033[m.')
else:
    print(f'O número digitado {primo}.')
