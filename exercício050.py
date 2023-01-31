cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite o {}° número:'.format(c)))
    if num % 2 == 0:
        soma += num # é o mesmo que soma = num + num!
        cont = cont + 1
print('A soma dos {} números pares é {}'.format(cont, soma))
