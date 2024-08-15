from datetime import date
print('\033[1mDIFERENCIADOR DA MAIORIDADE:\033[m')
maioridade = 0
menoridade = 0
pessoas = 0
for c in range(1, 8):
    data = int(input(f'Em que ano a {c}º nasceu? '))
    pessoas += 1
    if date.today().year - data >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f'Das {pessoas} pessoas \033[1;33m{menoridade} são de menor\033[m e \033[1;35m{maioridade} são de maior\033[m. ')
