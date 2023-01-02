n1 = int(input('Digite um número para conversão: '))
n2 = int(input("1-para conversão em Binário.\n2-Para conversão em Octal.\n3-Para conversão em Hexadecimal.\nEscolha uma opção para conversão: "))

if n2 == 1:
    print('O número {} em binário é: {}'.format(n1, bin(n1)[2:]))
elif n2 == 2:
    print('O número {} em octal é: {}'.format(n1, oct(n1)[2:]))
elif n2 == 3:
    print('O númnero {} em hexadecimal é: {}'.format(n1, hex(n1)[2:]))
else:
    print('Digite uma opção válida tente novamente!')

