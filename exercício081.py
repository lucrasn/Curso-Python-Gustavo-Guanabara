num = []
pergunta = 'S'
while pergunta == 'S':
    num.append(int(input('Digite um valor: ')))
    # pergunta = str(input('Quer continuar? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()[0]
    # if pergunta in 'Nn':
        # break
    while True:
        pergunta = str(input('Quer continuar? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()[0]
        if pergunta in 'NS':
            break
num.sort(reverse=True)
print('-=-' * 20)
print(f'''Você digitou \033[1;33m{len(num)} elementos\033[m.
Os valores em \033[1;34mordem decrescente são {num}\033[m''')
if num.count(5) != 0:
    print('\033[1;35mO valor 5 foi encontrado na lista.\033[m')
else:
    print('\033[1;31mO valor 5 não foi encontrado na lista.\033[m')
