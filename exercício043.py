# IMC -> kg/m**2
peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em m? '))
imc = peso / (altura ** 2)
print(f'Seu IMC é \033[34m{imc:.1f}\033[m')
if imc < 18.5:
    print('Você está\033[33m abaixo do peso\033[m.')
elif 18.5 <= imc < 25:
    print('Você está no\033[32m peso\033[m ideal.')
elif 25 <= imc < 30:
    print('Você está em\033[33m sobrepeso\033[m.')
elif 30 <= imc < 40:
    print('Você está em\033[31m obesidade\033[m.')
else:
    print('Você está em\033[31m obesidade mórbida\033[m.')
