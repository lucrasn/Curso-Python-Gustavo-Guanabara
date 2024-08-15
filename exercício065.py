print('\033[1mMÉDIA, MAIOR E MENOR\033[m')
maior = menor = soma = div = a = 0
b = ''
# b = 'S'
# while b in 'Ss':
while b != 'N':
    a = int(input('Digite um número: '))
    b = str(input('Você quer continuar a digitar valores [\033[1;32mS\033[m/\033[1;31mN\033[m]? ')).strip().upper()
    print('-=-'*10)
    soma += a
    div += 1
    if div == 1:
        maior = a
        menor = a
    else:
        if a > maior:
            maior = a
        elif a < menor:
            menor = a
print(f'''Você digitou \033[1;32m{div}\033[m números.
A média dos números colocados é \033[1;35m{soma/div:.2f}\033[m
O maior número digitado foi \033[1;33m{maior}\033[m
O menor número digitado foi \033[1;33m{menor}\033[m''')
