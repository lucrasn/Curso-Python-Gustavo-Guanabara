print('\033[1;33mPEGANDO DADOS E PROCESSANDO DADOS\033[m')
# mulher menor de 20 anos
menos20 = 0
# fazendo a soma das idades para tirar a média
soma = 0
# nome do homem mais velho
nome = ''
# quem tem a maior idade entre os homens
maior = 0
nomemaior = ''
for c in range(1, 5):
    nome = str(input(f'Qual o nome da {c}º pessoa? ')).strip().lower()
    idade = int(input(f'Qual a idade da {c}º pessoa? '))
    sexo = str(input(f'Qual o sexo da {c}º pessoa? ')).strip().lower()
    print('-=-'*10)
    # fazendo a soma das idades para tirar a média
    soma += idade
    # mulher menor de 20 anos
    if sexo == 'feminino' and idade < 20:
        menos20 += 1
    # quem tem a maior idade entre os homens
    # if c == 1 and sexo in 'MASCULINO, Masculino, masculino'
    if c == 1 and sexo == 'masculino':
        maior = idade
        nomemaior = nome
    elif sexo == 'masculino' and idade > maior:
        maior = idade
        nomemaior = nome
# mostrando os resultados
print(f'\033[1;32mA média das idades é {soma / 4:.1f}.\033[m')
print(f'\033[1;34mO homem mais velho tem {maior} e se chama {nomemaior}.\033[m')
print(f'\033[1;35mAo todo são {menos20} mulheres com menos de 20 anos.\033[m')
