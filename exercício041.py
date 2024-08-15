from datetime import date
print('\033[1;34mCLASSES DA NATAÇÃO:\033[m')
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
print(f'O atleta tem \033[1;34m{idade} anos\033[m.')
if idade <= 9:
    print('Você é \033[1;34mMIRIM 1\033[m')
elif idade == 10:
    print('Você é \033[1;34mMIRIM 2\033[m')
elif idade == 11:
    print('Você é \033[1;34mPETIZ 1\033[m')
elif idade == 12:
    print('Você é \033[1;34mPETIZ 2\033[m')
elif idade == 13:
    print('Você é \033[1;34mINFANTIL 1\033[m')
elif idade == 14:
    print('Você é \033[1;34mINFANTIL 2\033[m')
elif idade == 15:
    print('Você é \033[1;34mJUVENIL 1\033[m')
elif idade == 16:
    print('Você é \033[1;34mJUVENIL 2\033[m')
elif idade == 17:
    print('Você é \033[1;34mJÚNIOR 1\033[m')
elif 18 <= idade <= 19:
    print('Você é \033[1;34mJÚNIOR 2\033[m')
elif 30 > idade >= 20:
    print('Você é \033[1;34mSÊNIOR\033[m')
elif idade >= 30:
    print('Você é \033[1;34mMASTER\033[m')
else:
    print('\033[1;31mVocê vai nascer ainda.\033[m')
