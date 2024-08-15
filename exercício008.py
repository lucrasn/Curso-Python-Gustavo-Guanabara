m = float(input('Quantos metros? '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print(f'\033[35m{km} quilômetros\033[m;\n\033[35m{hm} hectômetros\033[m;\n\033[35m{dam} decâmetros\033[m;'
      f'\n\033[36m{m} metro(s)\033[m;')
print(f'\033[35m{dm} decímetros\033[m;\n\033[35m{cm} centímetros\033[m;\n\033[35m{mm} milímetros\033[m;')
