x = int(input('Digite um número: '))
dobro = x * 2
triplo = x * 3
raiz = x ** (1/2)
print(f'O dobro do número digitado é \033[1;31m{dobro}\033[m.\nO triplo do número digitado é \033[1;33m{triplo}\033[m'
      f'.\nA raiz quadrada do número digitado é \033[1;36m{raiz:.2f}\033[m.')
