def area(a, b):
    print('-=' * 17)
    print(f'A área do um terreno \033[1;34m{a}\033[mx\033[1;33m{b}\033[m é de \033[1;35m{a * b:.1f}m²\033[m')


print('\033[1;31mCONTROLE DE TERRENOS:\033[m')
print('-=' * 17)
area(float(input('Comprimento do terreno em metros: ')),
     float(input('Largura do terreno em metros: ')))
