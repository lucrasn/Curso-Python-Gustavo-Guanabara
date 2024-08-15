# tupla = (int(input('Primeiro número: ')), int(input('Segundo número: ')),
#         int(input('Terceiro número: ')), int(input('Quarto número: ')))
a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
d = int(input('Quarto número: '))
tupla = (a, b, c, d)
print(f'No total foram digitados \033[1;32m{tupla.count(9)} números 9\033[m.')
if tupla.count(3) > 0:
    print(f'O \033[1;33mprimeiro número 3 a ser digitado foi o {tupla.index(3) + 1}º número\033[m.')
else:
    print('O número 3 \033[1;31mnão foi digitado\033[m.')
print('Os \033[1;34mnúmeros pares digitados foram: ', end='')
for c in range(0, 4):
    if tupla[c] % 2 == 0:
        print(tupla[c], end=' ')
