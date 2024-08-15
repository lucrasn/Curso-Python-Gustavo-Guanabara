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


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[1;33m{c}\033[m - \033[1;34m{item}\033[m')
        c += 1
    print(linha())
    opc = leia_int('\033[1;32mSua Opção: \033[m')
    return opc
