from emoji import emojize
from random import choice
# from random import randint
# from time import sleep
print('Pesei num número de \033[34m0\033[m a \033[33m5\033[m tente adivinhar!')
# x = randint(0, 5)
x = choice([0, 1, 2, 3, 4, 5])
y = int(input('Em que número pensei? '))
# print('PROCESSANDO...')
# sleep(3) -> tá em segundos
if x == y:
    print(emojize('\033[1;32mPARABÉNS\033[m você conseguiu me vencer :rosto_festivo:!', language='pt'))
else:
    print(emojize(f'Mais sorte da proxima vez :rosto_chorando_aos_berros:, eu pensei no número '
                  f'\033[1;31m{x}\033[m.', language='pt'))
