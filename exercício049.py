'''
num = int(input('Digite um número para ver sua tabuada:'))
for c in range(1, 11):
    print('{} X {} = {}'.format(num, c, num*c))
 '''



n1 = int(input('Digite um número:'))
cont = 0
num = 0
for n in range(0, 11):
    num = cont * n1
    cont = cont + 1
    print('{} X {:2} = {}'.format(n1, n, num))
