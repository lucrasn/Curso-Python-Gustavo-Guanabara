num = int(input('Digite um número qualquer do sistema decimal: '))
# mostrando o que cada número significa
print('''\033[1;34mBASE DE CONVERSÃO\033[m:
Digite \033[1;33m1\033[m para\033[1;33m binário\033[m
Digite \033[1;35m2\033[m para\033[1;35m octal\033[m
Digite \033[1;31m3\033[m para\033[1;31m hexadecimal\033[m''')
base = int(input('Qual conversão de base? '))
# convertendo os números
if base == 1:
    print(f'O número \033[1;32m{num}\033[m em binário é assim \033[1;33m{bin(num)[2:]}\033[m.')
elif base == 2:
    print(f'O número \033[1;32m{num}\033[m em octal é assim \033[1;35m{oct(num)[2:]}\033[m.')
elif base == 3:
    hexadecimal = hex(num)
    print(f'O número \033[1;32m{num}\033[m em hexadecimal é assim \033[1;31m{hexadecimal.upper()[2:]}\033[m.')
else:
    print('Opção inválida. Tente novamente.')
