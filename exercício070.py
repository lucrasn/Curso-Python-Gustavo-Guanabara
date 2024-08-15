print('\033[1;31mCAIXINHA DO MERCADO\033[m')
print('-=-'*7)
a = b = barato = c1 = 0
c = pergunta = ''
while True:
    nome = str(input('Qual o\033[1;34m nome do produto\033[m? ')).strip()
    preco = float(input(f'Qual o\033[1;35m preço\033[m do(a) \033[1;35m{nome}\033[m? R$'))
    c1 += 1
    a += preco
    if preco > 1000:
        b += 1
    # if c1 == 1 or preco < menor: → ja que as duas condições a baixo são iguais da para simplificar desse forma
    if c1 == 1:
        barato = preco
        c = nome
    elif preco < barato:
        barato = preco
        c = nome
    print('-=-' * 7)
    # pergunta = ' '
    # while pergunta not in 'SN':
    pergunta = str(input('Você quer adicionar mair um produto? [\033[1;36mS\033[m/\033[1;33mN\033[m] '
                         '')).upper().strip()[0]
    while pergunta != 'S' and pergunta != 'N':
        pergunta = (str(input('Você quer adicionar mair um produto? [\033[1;36mS\033[m/\033[1;33mN\033[m] '
                              '')).upper().strip())[0]
    if pergunta == 'N':
        print('-=-' * 7)
        break
    print('-=-' * 7)
print(f'''\033[1;35mO total gasto será: R${a:.2f}\033[m;
\033[1;32m{b} produtos custam mais que R$1000.00\033[m;
\033[1;34mE produto mais barato comprado foi o(a) {c} que custa R${barato:.2f}.\033[m''')
