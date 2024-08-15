C = float(input('Informe a temperatura em ºC: '))
K = C + 273.15
F = C * 1.8 + 32
print(f'A temperatura de \033[32m{C}ºC\033[m corresponde a \033[34m{K}K\033[m e a \033[31m{F:.2f}ºF\033[m!')
