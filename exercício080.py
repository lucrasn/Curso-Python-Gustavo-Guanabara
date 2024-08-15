numeros = []
for c in range(1, 6):
    x = int(input(f'Digite o \033[1;32m{c}ª\033[m número: '))
    # if c == 1 or x > numeros[-1]:
    if c == 1 or max(numeros) < x:
        numeros.append(x)
        print('\033[1;33mAdicionado ao final da lista...\033[m')
    else:
        y = 0
        while y < len(numeros):
            if x <= numeros[y]:
                numeros.insert(y, x)
                print(f'\033[1;34mAdicionado na posição \033[m\033[1;35m{y}\033[m\033[1;34m da lista...\033[m')
                break
            y += 1
print('-=-' * 20)
print(f'\033[1;35mOs valores digitados em ordem foram: {numeros}\033[m')
