print('\033[1;34mCALCULADOR DE MÉDIA:\033[m')
a = float(input('Nota 1: '))
b = float(input('Nota 2: '))
c = (a + b) / 2
if c < 5.0:
    print('\033[1;31mALUNO REPROVADO\033[m')
elif 5.0 <= c <= 6.9:
    print('\033[1;33mALUNO EM RECUPERAÇÃO\033[m')
else:
    print('\033[1;32mALUNO APROVADO\033[m')
print(f'A nota média do aluno foi {c:.1f}.')
