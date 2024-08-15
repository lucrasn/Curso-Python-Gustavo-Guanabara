nome = str(input('Digite seu nome completo: ').strip())
print(f'''Seu primeiro nome é: \033[34m{nome.split()[0]}\033[m
Seu último nome é: \033[33m{nome.split()[-1]}\033[m''')
# nome = n.split()
# print(f'Seu último nome é: {nome[len(nome)-1]}')
