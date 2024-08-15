# temp = []
# dados = []
# mai = men = 0
# while True:
    # temp.append(str(input('Nome: ')))
    # temp.append(str(input('Peso: ')))
    # if len(dados) == 0:
        # mai = men = temp[1]
    # else:
        # if temp[1] > mai:
            # mai = temp[1]
        # if temp[1] < men:
            # men = temp[1]
    # dados.append(temp[:])
    # temp.clear()
    # resp = str(input('Adicionar mais  uma pessoa? [S/N] '))
    # if resp in 'Nn':
        # break
peso = []
nome = []
nomemais = []
nomemenos = []
pergunta = 'S'
while pergunta == 'S':
    nome.append(str(input('\033[1mNome:\033[m ')))
    peso.append(float(input('\033[1mPeso:\033[m ')))
    while True:
        pergunta = str(input('Adicionar mais  uma pessoa? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()[0]
        if pergunta in 'SN':
            break
if peso.count(max(peso)) > 1:
    for a, c in enumerate(peso):
        if c == max(peso):
            nomemais.append(nome[a])
else:
    nomemais.append(nome[peso.index(max(peso))])
if peso.count(min(peso)) > 1:
    for a, c in enumerate(peso):
        if c == min(peso):
            nomemenos.append(nome[a])
else:
    nomemenos.append(nome[peso.index(min(peso))])
print(f'No total foram cadastradas \033[1;35m{len(nome)} pessoas\033[m.')
print(f'O peso mais pesado registrado foi \033[1;33m{max(peso)}Kg da(s) pessoa(s): {nomemais}\033[m')
# print(f'O peso mais pesado registrado foi {mai}Kg da(s) pessoa(s): ', end='')
# for p in dados:
    # if p[1] == mai:
        # print(f'{p[0]}', end=''
# print()
print(f'O peso mais leve registrado foi \033[1;34m{min(peso)}Kg da(s) pessoa(s): {nomemenos}\033[m')
# print(f'O peso mais leve registrado foi {mai}Kg da(s) pessoa(s): ', end='')
# for p in dados:
    # if p[1] == men:
        # print(f'{p[0]}', end=''
# print()
