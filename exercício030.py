x = int(input('Digite um número qualquer: ')) % 2
if x == 0:
    print('O número digitado é \033[1;34mPAR!\033[m')
else:
    print('O número digitado é \033[1;33mÍMPAR!\033[m')
