def fatorial(n=1, show=False):
    """
    -> Função que calcula o fatorial de um número.
    :param n: Número a ser calculado o fatorial
    :param show: (opcional) Valor boolean para mostra o processo de cálculo
    :return: O valor do fatorial de um número "n"
    """
    print('-=' * 15)
        # x = y = 1
        # while x <= n:
        # y *= x
        # x += 1
        # print(y)
    x = 1
    for y in range(n, 0, -1):
        x *= y
        if show:
            if y == 1:
                print(f'\033[1m{y}\033[m', end=' = ')
                break
            print(f'\033[1m{y}\033[m', end=' x ')
    return f'\033[1;34m{x}\033[m'


print(fatorial(5, True))
# help(fatorial)
