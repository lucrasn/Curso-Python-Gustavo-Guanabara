salario = float(input('Qual o seu salário? R$'))
if salario > 1250.00:
    aumento = salario * 1.1
else:
    aumento = salario * 1.15
print(f'Quem ganhava \033[32mR${salario:.2f}\033[m passa a ganhar \033[36mR${aumento:.2f}\033[m agora.')
