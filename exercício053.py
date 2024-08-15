print('\033[1;36mVERIFICADOR DE PALÍNDROMOS:\033[m')
frase1 = str(input('Digite uma frase qualquer sem acento e verifique se é um palíndromo: ')).lower().strip().split()
frase = ''.join(frase1)
seafra = frase[::-1]
# inverso = ''
# for letra in range(len(frase) - 1, -1, -1):
    # inverso += frase[letra]
if frase == seafra:
    print('A frase digitada\033[1;34m é um palíndromo\033[m.')
else:
    print('A frase digitada\33[1;31m não é um palíndromo\033[m.')
