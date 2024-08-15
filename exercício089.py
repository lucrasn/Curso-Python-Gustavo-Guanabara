from time import sleep
dados = []
alunos = []
nota = []
media = []
s = 'S'
# ficha = list()
# while True:
while s == 'S':
    # nome = str(input('Nome: '))
    alunos.append(str(input('Nome: ')))
    # nota1 = float(input('Nota 1: '))
    nota.append(float(input('Nota 1: ')))
    # nota2 = float(input('Nota 2: '))
    nota.append(float(input('Nota 2: ')))
    # media = (nota1 + nota2) / 2
    media.append((nota[0] + nota[1]) / 2)
    alunos.append(nota[:])
    # ficha.appen(nome, [nota1, nota2], media)
    dados.append(alunos[:])
    nota.clear()
    alunos.clear()
    # resp = str(input('Adicionar mais um aluno? [S/N] '))
    # if resp in 'Nn':
        # break
    while True:
        s = str(input('Adicionar mais um aluno? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()[0]
        if s in 'SN':
            break
print('-=-' * 11 + f'\n{'No. NOME':25}' + f'MÉDIA\n' + '=' * 31)
for a, b in enumerate(dados):
    # print(f'{a:<4}{b[0]:21}{a[2]:>4.1f}')
    print(f'\033[1m{a:<4}\033[m\033[1;34m{b[0]:21}\033[m\033[1;35m{media[a]:>4.1f}\033[m')
print('=' * 37)
while True:
    x = int(input('Digite o No. do aluno para mostrar sua nota \033[1;31m(999 interrompe)\033[m: '))
    if x == 999:
        break
    # if x <= len(ficha) - 1:
    print(f'As notas de \033[1;34m{dados[x][0]}\033[m são \033[1;33m{dados[x][1]}\033[m')
    print('=' * 37)
print('\033[1mFINALIZANDO...\033[m')
sleep(1)
print('\033[1;32m<<< VOLTE SEMPRE >>>\033[m')
