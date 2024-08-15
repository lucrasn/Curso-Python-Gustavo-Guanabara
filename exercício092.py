# from datetime import datetime
from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().lower().title()
# dados['idade'] = datetime.now().year - int(input('Ano de nascença: '))
dados['idade'] = date.today().year - int(input('Ano de nascença: '))
dados['ctps'] = int(input('CTPS (0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contrato'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (35 - (date.today().year - dados['contrato']))
print('-=-'*15)
print(f'''Seu nome é \033[1;32m{dados["nome"]}\033[m;
Com \033[1;33m{dados["idade"]} anos\033[m de idade;
Sua CTPS: \033[1;34m{dados["ctps"]}\033[m;''')
if dados['ctps'] != 0:
    print(f'''\033[1;35mContrado no ano de {dados["contrato"]}\033[m;
Ganhando um \033[1;36msalário de R${dados["salário"]:.2f}\033[m;
E se \033[1;31maposentará aos {dados["aposentadoria"]} de idade\033[m.''')
