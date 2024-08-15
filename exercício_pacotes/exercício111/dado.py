def leia_dinheiro(a):
    while True:
        valor = str(input(a)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[1;31mERRO: \'{valor.strip()}\' é um preço inválido\033[m')
        else:
            return float(valor)
