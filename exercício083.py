# a = [str(input('Digite uma expressão: '))]
# if a[0].count('(') == a[0].count(')'):
    # print('Sua expressão está válida!')
# elif a[0].count('(') != a[0].count(')'):
    # print('Sua expressão está errada!')
a = str(input('Digite uma expressão: '))
b = []
for c in a:
    if c == '(':
        b.append('(')
    elif c == ')':
        if len(b) > 0:
            b.pop()
        else:
            b.append(')')
            break
if len(b) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
