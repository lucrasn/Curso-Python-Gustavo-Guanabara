print(f'\033[1;32m{'CALCULADOR DE PREÇOS':=^40}\033[m')
preco = float(input('Qual o preço do produto? R$'))
print('\033[1;33mCONDIÇÃO DE PAGAMENTO:\033[m')
print('''Se for à vista ou débito digite \033[1;34m1\033[m.
Se for no crédito digite \033[1;34m2\033[m.
Se for parcelado em 2x no cartão digite \033[1;34m3\033[m.
Se for parcelado em 3x no cartão ou mais digite \033[1;34m4\033[m.''')
pagamento = str(input('Forma de pagamento: ')).strip()
if pagamento == '1':
    print(f'O produto sai por \033[1;35mR${preco * 0.9:.2f}\033[m')
elif pagamento == '2':
    print(f'O produto sai por \033[1;35mR${preco * 0.95:.2f}')
elif pagamento == '3':
    print(f'O produto sai por \033[1;35mR${preco:.2f}\033[m')
    print(f'Pagando \033[1;35m2x de R${preco / 2:.2f} SEM JUROS\033[m')
elif pagamento == '4':
    parcela = int(input('Quantas parcelas? '))
    print(f'O produto sai por \033[1;35mR${preco * 1.2:.2f}\033[m')
    print(f'Pagando \033[1;35m7x de R${(preco * 1.2) / parcela:.2f}\033[m')
else:
    print('\033[1;31mVocê não digitou uma forma de pagamento valida.\033[m')
