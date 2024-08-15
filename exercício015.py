dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos quilômetros rodados? '))
# R$60 por dia e R$0.15 por km rodado
print(f'O total a pagar é de \033[1;31mR${(dia * 60) + (km * 0.15):.2f}\033[m')
