reais = float(input('Quanto dinheiro você tem na carteira? R$'))
dollar = reais / 4.95
print(f'Com \033[1;32mR${reais:.2f}\033[m você pode comprar \033[1;34mUS${dollar:.2f}\033[m')
