nota1 = float(input('Primeira nota do aluno: '))
nota2 = float(input('Segunda nota do aluno: '))
media = (nota1 + nota2) / 2
cor = {'nota': '\033[1;34m'}
if media < 7:
    cor = {'nota': '\033[1;31m'}
print(f'Sua média é: {cor['nota']}{media:.1f}')
