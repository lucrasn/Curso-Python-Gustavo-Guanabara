print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
x = '\033[31mNÃO PODEM FORMAR'
# if a < b + c and b < a + c and c < b + a:
if b < a < b + c and a > c:
    x = '\033[32mPODEM FORMAR'
if a < b < a + c and b > c:
    x = '\033[32mPODEM FORMAR'
if a < c < a + b and c > b:
    x = '\033[32mPODEM FORMAR'
if a == c == b:
    x = '\033[32mPODEM FORMAR'
print(f'Os segmentos acima {x}\033[m um triângulo.')
