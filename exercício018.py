from math import cos, sin, tan, radians
grau = int(input('Coloque um ângulo em graus para saber seu cos, sen e tan: '))
radi = radians(grau)
print(f'Para um ângulo de \033[32m{grau}º\033[m temos:\nSeno: \033[34m{sin(radi):.2f}\033[m'
      f'\nCosseno: \033[33m{cos(radi):.2f}\033[m \nTangente: \033[35m{tan(radi):.2f}\033[m')
