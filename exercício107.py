from exercício_pacotes import moeda

n = float(input('Digite o preço: R$'))
print(f'''A \033[1;33mmetade de R${n:.2f}\033[m é \033[1;33mR${moeda.metade(n):.2f}\033[m
O \033[1;35mdobro de R${n:.2f}\033[m é \033[1;35mR${moeda.dobro(n):.2f}\033[m
\033[1;31mAumentando 10%\033[m, temos \033[1;31mR${moeda.aumentar(n, 10):.2f}\033[m
\033[1;34mReduzindo 13%\033[m, temos \033[1;34mR${moeda.diminuir(n, 13):.2f}\033[m''')
