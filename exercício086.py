# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz = []
# for l in range(0, 3):
    # for c in range(0, 3):
        # matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: ')
for c1 in range(0, 3):
    matriz.append(int(input(f'Digite um valor para \033[1;34m[1, {c1}]\033[m: ')))
for c2 in range(0, 3):
    matriz.append(int(input(f'Digite um valor para \033[1;33m[2, {c2}]\033[m: ')))
for c3 in range(0, 3):
    matriz.append(int(input(f'Digite um valor para \033[1;35m[3, {c3}]\033[m: ')))
print('-=-'*10)
# for l in range(0, 3):
    # for c in range(0, 3):
        # print(f'[{matriz[l][c]:^5}]', end='')
    # print()
print(f'''\033[1;34m[{matriz[0]:^5}][{matriz[1]:^5}][{matriz[2]:^5}]\033[m
\033[1;33m[{matriz[3]:^5}][{matriz[4]:^5}][{matriz[5]:^5}]\033[m
\033[1;35m[{matriz[6]:^5}][{matriz[7]:^5}][{matriz[8]:^5}]\033[m''')
