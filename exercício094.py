cadastro = dict()
dados = []
a = b = 0
c = list()
d = list()
while True:
    a += 1
    cadastro['nome'] = (str(input('Nome: ')).strip().lower().title())
    while True:
        cadastro['sexo'] = (str(input('Sexo [\033[1;34mM\033[m/\033[1;33mF\033[m]: ')).strip().upper()[0])
        if cadastro['sexo'] in 'MF':
            break
        print('\033[1;31mERRO!\033[m Por favor, digite apenas \033[1;34mM\033[m ou \033[1;33mF\033[m.')
    if cadastro['sexo'] == 'F':
        c.append(cadastro['nome'])
    cadastro['idade'] = (int(input('Idade: ')))
    b += cadastro['idade']
    dados.append(cadastro.copy())
    while True:
        resp = str(input('Deseja adicionar mais uma pessoa? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).strip()[0]
        if resp in 'SsNn':
            break
        print('\033[1;31mERRO!\033[m Por favor, digite apenas \033[1;32mS\033[m ou \033[1;31mN\033[m.')
    print('-='*25)
    if resp in 'Nn':
        break
for x in range(0, len(dados)):
    if dados[x]["idade"] > (b / a):
        d.append(dados[x]["nome"])
# A) print(f'No total foram {len(dados)} pessoas cadastradas')
# C) print('As mulheres cadastradas foram ', end='')
# for c in dados:
    # if c['sexo'] == 'F':
        # print(f'{p["nome"]}, ', end='')
# print()
# D) print(As pessoas com idade a cima da média foram: ')
#  for c in dados:
    # if c['idade'] >= (b / a):
        # for k, v in c.items():
            # print(f'  {k} = {v}: ', end='')
        # print()
print(f'''\033[1;35mNo total foram {a} pessoas cadastradas\033[m;
\033[1;32mA média das idades é {b / a:.2f} anos\033[m;
\033[1;33mAs mulheres cadastradas foram {c}\033[m;
\033[1;31mAs pessoas com idade a cima da média foram: {d}\033[m.''')
print('\033[1m<< ENCERRADO >>\033[m')
