from math import trunc
num = float(input('Escreva um número: '))
print(f'O número \033[1;32m{num}\033[m tem a parte inteira \033[1;35m{trunc(num)}\033[m')
# num = float(input('Digite um número: '))
# print(f'{num} tem sua parte inteira como sendo {int(num)}')
# ou ainda print(f'{num} tem sua parte inteira como sendo {:.0f}')
