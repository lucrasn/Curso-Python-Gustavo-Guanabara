numero = []
# maior = menor = 0
for a in range(0, 5):
    numero.append(int(input(f'Digite um valor para a\033[1;34m posição {a}\033[m: ')))
    # if a == 0:
        # maior = menor = numero[a]
    # else:
        # if numero[a] > maior:
            # maior = numero[a]
        # if numero[a] < menor:
            # menor = numero[a]
print('=-'*20)
print(f'Você digitou os valores \033[1;34m{numero}\033[m')
print(f'O\033[1;35m maior valor digitado foi {max(numero)}\033[m nas posições ', end='')
# for i, v enumerate(numero):
    # if v == maior:
        # print(f'{i}... ', end='')
for b, c in enumerate(numero):
    if c == max(numero):
        print(f'\033[1;35m{b}\033[m... ', end='')
print(f'\nO\033[1;33m menor valor digitado foi {min(numero)}\033[m nas posições ', end='')
# for i, v enumerate(numero):
    # if v == menor:
        # print(f'{i}... ', end='')
for b, c in enumerate(numero):
    if c == min(numero):
        print(f'\033[1;33m{b}\033[m... ', end='')
print()
