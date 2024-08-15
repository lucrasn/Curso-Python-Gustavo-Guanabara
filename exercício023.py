# demorei nessa aqui viu difícil, difícil e difícil
numero = input('Digite qualquer número de 0 a 9999: ')
zeros = '000' + numero
print(f'''Unidade: \033[31m{zeros[-1]}\033[m
Dezena: \033[32m{zeros[-2]}\033[m
Centena: \033[33m{zeros[-3]}\033[m
Milhar: \033[34m{zeros[-4]}\033[m''')
# podia ter feito usando cálculos matemáticos:
# unidade seria x // 1 % 10;
# dezena seria y // 10 % 10;
# Centena seria w // 100 % 10;
# Milhar seira z // 1000 % 10.
