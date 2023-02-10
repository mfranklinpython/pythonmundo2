n1 = int(input('Digite um número: '))
cont = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' - ')
print('\n\033[mFim!')
print('\033[mO número {} foi divisível {} vezes.'.format(n1, cont))
