from emoji import emojize
from time import sleep
print('\033[1;32mCONTAGEM REGRESSIVA\033[m')
for c in range(10, -1, -1):
    print(c)
    if c > 0:
        sleep(1)
print(emojize(':confete::brilhos::rosto_festivo::cone_de_festa:', language='pt'))
