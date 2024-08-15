from datetime import date
print('\033[1;32mALISTAMENTO MILITAR:\033[m')
sexo = str(input('Você é do sexo masculino ou feminino: ')).upper().strip()
quero = 'NÃO'
if sexo == 'FEMININO':
    print('Você não é obrigada a fazer o alistamento militar!')
    quero = str(input('Pretende fazer mesmo assim: ')).upper().strip()
if sexo == 'MASCULINO' or quero == 'SIM':
    ano = int(input('Em que ano você nasceu? '))
    # pegando a date de hoje e subtraindo do ano de nascença para obter a idade
    idade = date.today().year - ano
    # verificando se deve se alistar ou não
    if idade == 18:
        print('Você deve fazer o alistamento militar \033[1;34mESSE ANO\033[m!')
    elif idade < 18:
        falta = 18 - idade
        print(f'Você deverá se alistar daqui a \033[1;33m{falta} ANO(S)\033[m.')
    else:
        passou = idade - 18
        year = date.today().year - passou
        print(f'Você ja deve ter se alistado no ano de \033[1;31m{year}\033[m')
print('Obrigado por consultar a junta militar.')
