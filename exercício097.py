def escreva(frase):
    print('\033[1;35m~\033[m' * (len(frase) + 4))
    print(f'  \033[1m{frase}\033[m')
    print('\033[1;35m~\033[m' * (len(frase) + 4))


escreva(str(input('Escreva uma mensagem qualquer: ')))
print()
