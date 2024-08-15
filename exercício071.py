print('\033[1;33mCAIXA ELETRÔNICO\033[m')
print('-=-'*14)
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
x = int(input('Qual valor será sacado? R$'))
print('Você receberá:')
# quantas notas de 50
a = x // 50
# tirando o valor de 50 do valor total
x -= a * 50
if a != 0:
    print(f'\033[1;31m{a} notas de R$50.00\033[m')
if x != 0:
    # quantas notas de 20
    b = x // 20
    # tirando o valor de 20 do valor total
    x -= b * 20
    if b != 0:
        print(f'\033[1;32m{b} notas de R$20.00\033[m')
    if x != 0:
        # quantas notas de 10
        c = x // 10
        # tirando o valor de 10 do valor total
        x -= c * 10
        if c != 0:
            print(f'\033[1;34m{c} notas de R$10.00\033[m')
        if x != 0:
            # quantas moedas de 1
            d = x
            print(f'\033[1;35m{d} moedas de R$1.00\033[m')
print('-=-'*14)

# jeito do Guanabara:
# valor = int(input('Que valor você quer sacar? R$'))
# total = valor
# ced = 50
# totced = 0
# while True:
    # if total >= ced:
        # total -= ced
        # totced += 1
    # else:
        # if totced > 0:
            # print(f'Total de {totced} cédulas de R${ced:.2f}')
        # if ced == 50:
            # ced = 20
        # elif ced == 20:
            # ced = 10
        # elif ced == 10:
            # ced = 1
        # totced = 0
        # if total == 0:
            # break
