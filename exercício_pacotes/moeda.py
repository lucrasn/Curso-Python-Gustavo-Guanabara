# exercício107
# exercício109 - adição do parâmetro c


def aumentar(a=0, b=100, c=False):
    d = a * (1 + (b / 100))
    # if c:
        # d = f'R${a * (1 + (b / 100)):.2f}'
    return d if c is False else moeda(d)


def diminuir(a=0, b=100, c=False):
    d = a * (1 - (b / 100))
    # if c:
        # d = f'R${a * (1 - (b / 100)):.2f}'
    return d if c is False else moeda(d)


def dobro(a=0, c=False):
    d = a * 2
    # if c:
        # d = f'R${a * 2:.2f}'
    return d if c is False else moeda(d)


def metade(a=0, c=False):
    d = a / 2
    # if c:
        # d = f'R${a / 2:.2f}'
    return d if c is False else moeda(d)


# exercício108


def moeda(a=0.0, tipo='R$'):
    return f'{tipo}{a:.2f}'.replace('.', ',')


# exercício110


def resumo(x=0, y=10, w=5):
    print('=' * 29)
    print(f'{"RESUMO DO VALOR":^29}')
    print('=' * 29)
    print(f'{"Preço analisado:":<20}\033[1m{moeda(x)}\033[m')
    print(f'{"Dobro do preço:":<20}\033[1;35m{dobro(x, True)}\033[m')
    print(f'{"Metade do preço:":<20}\033[1;33m{metade(x, True)}\033[m')
    print(f'{f"{y}% de aumento:":<20}\033[1;31m{aumentar(x, y, True)}\033[m')
    print(f'{f"{w}% de desconto:":<20}\033[1;34m{diminuir(x, w, True)}\033[m')
    print('=' * 29)
