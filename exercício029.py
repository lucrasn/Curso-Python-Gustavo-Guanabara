velo = float(input('Qual a velocidade do seu carro em km/h? '))
if velo > 80:
    # multa custa R$7.00 por casa km acima do limite
    multa = (velo - 80) * 7
    print('Devido ao excedente na velocidade permitida você será \033[1;31mmultado\033[m.')
    print(f'Devera pagar uma multa de \033[1;31mR${multa:.2f}\033[m')
else:
    print('Parabéns você esta dentro do limite de \033[1;34mvelocidade permitido\033[m.')
