print('\033[1mEMPRÉSTIMO PARA FINANCIAR UMA CASA\033[m')
print('-='*18)
# perguntando dados
valor = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
meses = int(input('Quantos anos de financiamento? ')) * 12
prestacao = valor / meses
# verificando seu pode fazer o empréstimo
if valor / meses > salario * 0.3:
    print(f'Infelizmente seu pedido de empréstimo foi\033[1;31m NEGADO\033[m, '
          f'devido a\033[1;31m prestação mensal ultrapassar 30%\033[m do seu salário.')
else:
    print(f'Pedido de empréstimo\033[1;34m APROVADO\033[m,'
          f' sua prestação mensal irá custar\033[1;34m R${prestacao:.2f}\033[m!')
print('Tenha um bom dia!')
