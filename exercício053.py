frase = str(input('Digite sua frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto[::-1] <===> modo de ser feito sem for
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
