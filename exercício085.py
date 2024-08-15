numeros = [[], []]
for w in range(1, 8):
    x = int(input(f'\033[1;35m{w}ª\033[m\033[1m valor\033[m: '))
    if x % 2 == 0:
        numeros[0].append(x)
    else:
        numeros[1].append(x)
numeros[0].sort()
numeros[1].sort()
print('-=-'*15)
print(f'''Foram digitados \033[1;34m{len(numeros[0])} números pares: {numeros[0]}\033[m
Foram digitados \033[1;33m{len(numeros[1])} números ímpares: {numeros[1]}\033[m''')
