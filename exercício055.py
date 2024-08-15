print('\033[1;35mLEITOR DE PESOS:\033[m')
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa: (kg)'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O\033[1;34m maior peso lido\033[m foi de \033[1;34m{maior}kg\033[m')
print(f'O\033[1;33m menor peso lido\033[m foi de \033[1;33m{menor}kg\033[m')
