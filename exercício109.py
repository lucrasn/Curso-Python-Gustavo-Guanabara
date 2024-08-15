from exercício_pacotes import moeda

n = float(input('Digite o preço: R$'))
print(f'''A \033[1;33mmetade de {moeda.moeda(n)}\033[m é \033[1;33m{moeda.metade(n, True)}\033[m
O \033[1;35mdobro de {moeda.moeda(n)}\033[m é \033[1;35m{moeda.dobro(n, True)}\033[m
\033[1;31mAumentando 10%\033[m, temos \033[1;31m{moeda.aumentar(n, 10, True)}\033[m
\033[1;34mReduzindo 13%\033[m, temos \033[1;34m{moeda.diminuir(n, 13, True)}\033[m''')
