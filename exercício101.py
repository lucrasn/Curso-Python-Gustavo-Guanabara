def voto(a):
    from datetime import datetime
    i = datetime.now().year - a
    votar = ''
    if 18 <= i <= 70:
        votar = '\033[1;34mVOTO OBRIGATÓRIO\033[m'
    elif 16 > i:
        votar = '\033[1;31mNÃO VOTA\033[m'
    elif 16 <= i < 18 or i > 70:
        votar = '\033[1;33mVOTO OPCIONAL\033[m'
    print(f'Com {i} anos: {votar}')


print('=-=' * 12)
voto(int(input('Em que ano você nasceu? ')))
