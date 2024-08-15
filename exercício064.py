print('\033[1;32mCONTADOR E SOMADOR DE NÚMEROS\033[m')
cont = soma = 0
print('\033[1;31mDIGITE 999 PARA SAIR\033[m')
num = int(input('Digite um número inteiro: '))
print('-=-'*10)
while not num == 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro: '))
    print('-=-'*10)
# print(f'O total de números digitados foi {cont-1}. A soma dos números digitados deu {soma-999}.')
print(f'''O\033[1;34m total de números digitados foi {cont}.\033[m
A\033[1;35m soma dos números digitados deu {soma}\033[m.''')
