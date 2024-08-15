contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
            'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
# numero = int(input('Digite um número entre 0 e 20: '))
# while numero > 20 or numero < 0:
#   numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))
while True:
    numero = int(input('Digite um número entre \033[1;34m0\033[m e \033[1;34m20\033[m: '))
    if 20 >= numero >= 0:
        print(f'Você digitou o número \033[1;35m{contagem[numero]}\033[m.')
        resposta = str(input('Você deseja continuar? [\033[1;32mS\033[m/\033[1;31mN\033[m]')).upper().strip()[0]
        if resposta == 'N':
            break
    print('\033[1;33mTente novamente.\033[m ', end='')
