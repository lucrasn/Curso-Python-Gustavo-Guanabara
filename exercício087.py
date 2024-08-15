matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para \033[1;31m[{linha}, {coluna}]\033[m: '))
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
print('-=-' * 10)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[\033[1;31m{matriz[linha][coluna]:^5}\033[m]', end='')
    print()
print('-=-' * 10)
print(f'A \033[1;34msoma dos valores pares\033[m é \033[1;34m{soma_par}\033[m.')
# soma_3coluna = 0
# for linha in range(0, 3):
    # soma_3coluna += matriz[linha][2]
# print(f'A soma dos valores da terceira coluna é {soma_3coluna}.')
print(f'A \033[1;35msoma dos valores da terceira coluna\033[m é \033[1;35m{matriz[0][2] + matriz[1][2] + matriz[2][2]}'
      f'\033[m.')
# mai = 0
# for c in range(0, 3):
    # if c == 0 or matriz[1][c] > mai:
        # mai = matriz[1][c]
# print(f'O maior valor da segunda linha é {mai}')
print(f'O \033[1;33mmaior valor da segunda linha\033[m é \033[1;33m{max(matriz[1])}\033[m')
