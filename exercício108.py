from exercício_pacotes import moeda

n = float(input('Digite o preço: R$'))
print(f'''A metade de \033[1;33m{moeda.moeda(n)}\033[m é \033[1;33m{moeda.moeda(moeda.metade(n))}\033[m
O dobro de \033[1;35m{moeda.moeda(n)}\033[m é \033[1;35m{moeda.moeda(moeda.dobro(n))}\033[m
\033[1;31mAumentando 10%\033[m, temos \033[1;31m{moeda.moeda(moeda.aumentar(n, 10))}\033[m
\033[1;34mReduzindo 13%\033[m, temos \033[1;34m{moeda.moeda(moeda.diminuir(n, 13))}\033[m''')
