# geral = list()
geral = []
pergunta = 'S'
while pergunta == 'S':
    geral.append(int(input('Digite um número: ')))
    while True:
        pergunta = str(input('Quer continuar? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()[0]
        if pergunta in 'SN':
            break
par = []
impar = []
# for c, g in enumerate(geral):
for g in geral:
    if g % 2 == 0:
        par.append(g)
    else:
        impar.append(g)
print('-=-' * 15)
print(f'''\033[1;34mA lista completa é {geral}\033[m
\033[1;35mA lista de pares é {par}\033[m
\033[1;33mA lista de ímpares é {impar}\033[m''')
