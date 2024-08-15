# from datetime import date
# ano = int(input('Digite um ano e descubra de ele é bissexto. Coloque 0 para analisar o ano atual: '))
ano = int(input('Digite um ano e descubra de ele é bissexto: '))
# if ano == 0:
    # ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'\033[1;34mO ano {ano} É BISSEXTO!\033[m')
else:
    print(f'\033[1;31mO ano {ano} NÃO é bissexto!\033[m')
