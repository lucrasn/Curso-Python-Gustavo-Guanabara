def leia_int(x):
    while True:
        y = input(x)
        if y.isnumeric():
            y = int(y)
            return y
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido\033[m')


n = leia_int('Digite um número: ')
print(f'Você acabou de digitar o número \033[1;35m{n}\033[m')

# Guanabara ->
# def leia_int(msg):
    # ok = False
    # valor = 0
    # while True:
        # n = str(input(msg))
        # if n.isnumeric():
            # valor = int(n)
            # ok = True
        # else:
            # print('ERRO! Digite um número inteiro válido')
        # if ok:
            # break
    # return valor
