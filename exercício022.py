nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
# linha 7 → podia ser feita assim: ...{len(nome) - nome.count(' ')}
# linha 8 → podia ser feita assim: ...{nome.find(' ')}
print(f'''Seu nome em maiúsculo: \033[33m{nome.upper()}\033[m
Seu nome em minúsculo: \033[35m{nome.lower()}\033[m
Número de letra do seu nome: \033[34m{len(''.join(lista))}\033[m
Quantas letras tem o seu primeiro nome: \033[31m{len(lista[0])}\033[m''')
