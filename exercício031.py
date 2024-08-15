km = float(input('Qual a distância da sua viaja em km? '))
p = km * 0.5 if km <= 200 else km * 0.45
print(f'A sua passagem sairá por \033[36mR${p:.2f}\033[m')
