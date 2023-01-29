n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 == n2 == n3:
    print('Esse é um triângulo EQUILÁTERO!')
elif n1 == n2 or n1 == n3 or n2 == n3:
    print('Esse é um triângulo ISÓSCELES!')
elif n1 + n2 <= n3 or n1 + n3 <= n2 or n2 + n3 <= n1:
    print('Não é possível obter um TRIÂNGULO!')
else:
    print('Esse é um triângulo ESCALENO!')
