def leia_int(x):
    while True:
        try:
            y = int(input(x))
        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu  não digitar esse número.\033[m')
            return 0
        else:
            return y


def leia_float(x):
    while True:
        try:
            y = float(input(x))
        except ValueError:
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu  não digitar esse número.\033[m')
            return 0
        else:
            return y


i = leia_int('Digite um número inteiro: ')
f = leia_float('Digite um número real: ')
print(f'Você acabou de digitar o número\033[1;35m inteiro {i}\033[m e\033[1;34m real {f}\033[m')
