tupla = ('laurentino', 'piauiense', 'gamer', 'python', 'new jeans')
# vogais = ('a', 'e', 'i', 'o', 'u')
# for item in range(0, len(tupla)):
    # print(f'\nA palavra {tupla[item]} tem as vogais: ', end='')
    # for loop_vogal in vogais:
        # numero_vogal = tupla[item].count(loop_vogal)
        # if numero_vogal > 0:
            # local_vogal = tupla[item].index(loop_vogal)
            # print(f'{tupla[item][local_vogal]}', end=' ')
for palavra in tupla:
    print(f'\nNa palavra \033[1;34m{palavra.upper()}\033[m temos: ', end='')
    for vogal in palavra:
        if vogal.lower() in 'aeiou':
            print(f'\033[1;35m{vogal}\033[m', end=' ')
