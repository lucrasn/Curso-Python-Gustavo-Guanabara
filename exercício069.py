a = b = c = 0
while True:
    print('===' * 9)
    print('    \033[1;32mCADASTRE UMA PESSOA\033[m')
    print('===' * 9)
    idade = int(input('Idade: '))
    if idade > 18:
        a += 1
    # sexo = ' '
    sexo = str(input('Sexo: [\033[1;34mM\033[m/\033[1;33mF\033[m] ')).upper().strip()[0]
    # while sexo not in 'MF':
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Sexo: [\033[1;34mM\033[m/\033[1;33mF\033[m] ')).upper().strip()[0]
    if sexo == 'M':
        b += 1
    elif sexo == 'F' and idade < 20:
        c += 1
    print('===' * 9)
    continuar = str(input('Quer continuar? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Quer continuar? [\033[1;32mS\033[m/\033[1;31mN\033[m] ')).upper().strip()
    if continuar == 'N':
        print('===' * 9)
        break
print('\033[1;31mFIM DO PROGRAMA\033[m')
print(f'''Total de\033[1;35m pessoas com mais de 18 anos: {a}\033[m;
Ao todo temos \033[1;34m{b} homens\033[m cadastrados;
E temos \033[1;33m{c} mulheres com menos de 20 anos\033[m.''')
