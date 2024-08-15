from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
maior = menor = 0
print('Os números sorteados foram: ', end='')
for c in range(0, 5):
    if c == 0:
        maior = num[c]
        menor = num[c]
    else:
        if maior < num[c]:
            maior = num[c]
        elif menor > num[c]:
            menor = num[c]
    if c == 4:
        print(f'\033[1;35m{num[c]}\033[m')
        break
    print(f'\033[1;35m{num[c]}\033[m', end=', ')
# print(f'O maior valor sorteado foi {max(num)}')
# print(f'O menor valor sorteado foi {min(num)}')
print(f'''\033[1;33mO maior número é {maior}\033[m
\033[1;34mO menor número é {menor}\033[m''')
