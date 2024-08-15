largura = float(input('Qual é a largura da sua parede em metros? '))
altura = float(input('Qual é a altura da sua parede em metros? '))
area = largura * altura
tinta = area / 2
print(f'Para uma área de \033[1;35m{area}m²\033[m, considerando que um litro pinta 2.0m² você precisará de '
      f'\033[1;34m{tinta}L\033[m de tinta.')
