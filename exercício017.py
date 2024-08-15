from math import hypot
cat = float(input('Em centímetros, quanto mede o cateto oposto: '))
adj = float(input('Em centímetros, quanto mede o cateto adjacente: '))
# a soma dos catetos ao quadrado e igual a hipotenusa ao quadrado
print(f'Pelo teorema de Pitágoras com um cateto medindo \033[1;33m{cat}cm\033[m e o outro cateto com \033[1;34m{adj}cm '
      f'\033[ma hipotenusa mede \033[1;35m{hypot(cat, adj):.2f}cm\033[m!')
