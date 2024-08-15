frase = str(input('Escreva uma frase: ').strip().upper())
print(f'''Quantas letras A tem na sua frase: \033[31m{frase.count('A')}\033[m
A primeira letra A apareceu na posição \033[34m{frase.find('A') + 1}ª\033[m
A última letra A apareceu na posição \033[33m{frase.rfind('A') + 1}ª\033[m''')
