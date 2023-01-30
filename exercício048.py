soma = 0
contador = 0
for n in range(1, 501, 2):
    if n % 3 == 0:       
        soma = soma + n
        contador = contador + 1
print('A soma de todos os {} valores solicitados é {}.'.format(contador, soma))
