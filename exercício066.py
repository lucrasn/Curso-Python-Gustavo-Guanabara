print('\033[1;33mCONTADOR E SOMADOR DE NÚMEROS 2.0\033[m')
cont = soma = 0
print('\033[1;31mDIGITE 999 PARA SAIR\033[m')
print('-=-'*10)
while True:
    num = int(input('Digite um número inteiro: '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'''O\033[1;34m total de números digitados foi {cont}.\033[m
A\033[1;35m soma dos números digitados deu {soma}\033[m.''')
