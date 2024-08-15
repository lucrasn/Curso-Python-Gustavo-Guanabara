from random import choice
a = input('Nome do aluno 1: ')
b = input('Nome do aluno 2: ')
c = input('Nome do aluno 3: ')
d = input('Nome do aluno 4: ')
print(f'O aluno escolhido é \033[36m{choice([a, b, c, d])}\033[m!')
