numeros = []
while True:
    x = int(input('Digite um número inteiro: '))
    # if x not in números:
        # numeros.append()
        # print('Valor adicionado com sucesso!')
    # else:
        # print('Número duplicado não adicionado!')
    if numeros.count(x) >= 1:
        print('\033[1;31mNúmero duplicado não adicionado!\033[m')
    elif numeros.count(x) == 0:
        print('\033[1;34mValor adicionado com sucesso!\033[m')
        numeros.append(x)
    y = str(input('Você quer adicionar outro número? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()[0]
    if y not in 'SN':
        while True:
            print('\033[1;33mResposta inválida\033[m. Tente novamente...')
            y = str(input('Você quer adicionar outro número? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()[0]
            if y in 'SN':
                break
    # if y in 'Nn':
    if y == 'N':
        break
numeros.sort()
print(f'\033[1;35mVocê digitou os valores {numeros}\033[m')
