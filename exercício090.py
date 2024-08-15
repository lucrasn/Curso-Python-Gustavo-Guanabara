nome = str(input('Nome do aluno: '))
media = float(input(f'Média de {nome}: '))
dados = {'Nome': nome, 'Média': media}
if media >= 7:
    dados['Situação'] = '\033[1;32maprovado\033[m'
elif 7 > media >= 5:
    dados['Situação'] = '\033[1;33mrecuperação\033[m'
else:
    dados['Situação'] = '\033[1;31mreprovado\033[m'
print('-=-'*10)
for k, v in dados.items():
    print(f' - {k} é igual a \033[1;34m{v}\033[m')
