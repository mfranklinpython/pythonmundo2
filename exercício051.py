'''num = int(input('Digite um número: '))
pa = 0
print('A progressão aritimética de {}.'.format(num))
for c in range (0, 10, 1):
    pa = pa + num
    print('{}'.format(pa), end=' ')
'''
num = int(input('Digite primeiro termo:'))
pa = int(input('Digite a razão: '))
qtd = num + (10 - 1) * pa
print('Partindo do número {} com a razão sendo {} temos a PA: '.format(num, pa))
for c in range(num, qtd + pa, pa):
    print('{}'.format(c), end=' => ')
print('Fim!')
