cid = str(input('Digite um nome de uma cidade: ')).strip()
cid = cid.upper().split()
# print(cid[:5]).upper == 'SANTO')
print(f'A cidade começa com o nome \033[1;34mSanto\033[m? {'SANTO' in cid[0]}')
