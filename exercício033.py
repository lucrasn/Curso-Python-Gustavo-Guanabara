a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))
# Verificando quem é maior.
if a > b and a > c:
    print(f'O \033[35mMAIOR\033[m valor digitado foi \033[35m{a:.1f}\033[m.')
if b > a and b > c:
    print(f'O \033[35mMAIOR\033[m valor digitado foi \033[35m{b:.1f}\033[m.')
if c > a and c > b:
    print(f'O \033[35mMAIOR\033[m valor digitado foi \033[35m{c:.1f}\033[m.')
# Verificando quem é menor.
if a < b and a < c:
    print(f'O \033[36mMENOR\033[m valor digitado foi \033[36m{a:.1f}\033[m.')
if b < a and b < c:
    print(f'O \033[36mMENOR\033[m valor digitado foi \033[36m{b:.1f}\033[m.')
if c < a and c < b:
    print(f'O \033[36mMENOR\033[m valor digitado foi \033[36m{c:.1f}\033[m.')
