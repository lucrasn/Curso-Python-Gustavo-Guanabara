print('\033[1mCOMPARADOR DE NÚMEROS')
print('\033[1;34m-=-'*10, '\033[m')
# quais números
a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
# condições para o número maior
if a > b:
    print(f'O número \033[1;33m{a}\033[m é o \033[1;34mMAIOR\033[m!')
elif b > a:
    print(f'O número \033[1;33m{b}\033[m é o \033[1;34mMAIOR\033[m!')
# os número iguais
else:
    print(f'\033[1;33mNão existe\033[m valor maior, os dois são\033[1;34m iguais\033[m.')
