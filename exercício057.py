print('\033[1;35mLEITOR DE INFORMAÇÃO\033[m')
sexo = str(input('Informe seu sexo: [\033[1;34mM\033[m/\033[1;33mF\033[m] ')).upper().strip()
# sexo = str(input('Informe seu sexo: [\033[1;34mM\033[m/\033[1;33mF\033[m] ')).upper().strip()[0]
    # esse '[0]' é pra pegar a primeira letra
while not sexo == 'M' and not sexo == 'F':
    sexo = str(input('\033[1;31mDados inválidos\033[m. Por favor, informe seu sexo: ')).strip().upper()
    # sexo = str(input('\033[1;31mDados inválidos\033[m. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'\033[1;32mSexo {sexo} registrado com sucesso.\033[m')
