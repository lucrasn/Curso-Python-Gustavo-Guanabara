preco = float(input('Qual é o preço do produto? R$'))
desconto = preco * 0.95
print(f'Esse produto com \033[1;34m5%\033[m de desconto ficará com o preço de \033[1;34mR${desconto:.2f}\033[m.')
