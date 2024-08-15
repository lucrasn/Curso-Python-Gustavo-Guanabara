# exercício107
# exercício109 - adição do parâmetro c


def aumentar(a=0, b=100, c=False):
    """
    -> Aumento de um valor.
    :param a: Valor.
    :param b: Porcentagem.
    :param c: Conversão para moeda em reais.
    :return: Retorna o valor com o aumento.
    """
    d = a * (1 + (b / 100))
    # if c:
        # d = f'R${a * (1 + (b / 100)):.2f}'
    return d if c is False else moeda(d)


def diminuir(a=0, b=100, c=False):
    """
    -> Desconto de um valor.
    :param a: Valor.
    :param b: Porcentagem.
    :param c: Conversão para a moeda em reais.
    :return: Retorna o valor com o desconto.
    """
    d = a * (1 - (b / 100))
    # if c:
        # d = f'R${a * (1 - (b / 100)):.2f}'
    return d if c is False else moeda(d)


def dobro(a=0, c=False):
    """
    -> Dobra o número.
    :param a: Número.
    :param c: Conversão para a moeda em reais.
    :return: Retorna o valor dobrado.
    """
    d = a * 2
    # if c:
        # d = f'R${a * 2:.2f}'
    return d if c is False else moeda(d)


def metade(a=0, c=False):
    """
    -> Divide o valor por 2.
    :param a: Valor.
    :param c: Conversão para a moeda em reais.
    :return: Retorna a metade do valor.
    """
    d = a / 2
    # if c:
        # d = f'R${a / 2:.2f}'
    return d if c is False else moeda(d)


# exercício108


def moeda(a=0.0, tipo='R$'):
    """
    -> Apresenta o valor em monetário.
    :param a: Valor.
    :param tipo: Moeda a ser convertida (R$ padrão)
    :return: O valor em monetário
    """
    return f'{tipo}{a:.2f}'.replace('.', ',')


# exercício110


def resumo(x=0, y=10, w=5):
    """
    -> Apresenta o resumo do valor: metade(), dobro(), aumento() e diminuir()
    :param x: Valor.
    :param y: Porcentagem de aumento (10% por padrão).
    :param w: Porcentagem de desconto (5% por padrão).
    :return: Retorna todos os valores convertidos.
    """
    print('=' * 29)
    print(f'{"RESUMO DO VALOR":^29}')
    print('=' * 29)
    print(f'{"Preço analisado:":<20}\033[1m{moeda(x)}\033[m')
    print(f'{"Dobro do preço:":<20}\033[1;35m{dobro(x, True)}\033[m')
    print(f'{"Metade do preço:":<20}\033[1;33m{metade(x, True)}\033[m')
    print(f'{f"{y}% de aumento:":<20}\033[1;31m{aumentar(x, y, True)}\033[m')
    print(f'{f"{w}% de desconto:":<20}\033[1;34m{diminuir(x, w, True)}\033[m')
    print('=' * 29)
