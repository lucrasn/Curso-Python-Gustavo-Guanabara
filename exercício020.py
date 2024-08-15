from random import sample
a = input('Nome do aluno 1: ')
b = input('Nome do aluno 2: ')
c = input('Nome do aluno 3: ')
d = input('Nome do aluno 4: ')
print(f'A ordem é \033[36m{sample([a, b, c, d], k=4)}\033[m')
# print(f'A ordem é {shuffle([a, b, c, d]}')
