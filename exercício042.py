print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < b + a:
    print('Os segmentos acima \033[32mPODEM FORMAR\033[m um triângulo.')
    if a == b == c:
        print('Formará um triângulo \033[1;34mEQUILÁTERO\033[m.')
    elif a == b or a == c or b == c:
        print('Formará um triângulo \033[1;34mISÓSCELES\033[m.')
    # elif a != b != c != a:
        # print('ESCALENO')
    else:
        print('Formará um triângulo \033[1;34mESCALENO\033[m.')
else:
    print('Os segmentos acima \033[31mNÃO PODEM FORMAR\033[m um triângulo.')
