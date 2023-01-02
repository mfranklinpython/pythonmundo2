casa = float(input('Digite o valor da casa R$ '))
salario = float(input('Digite o valor do Salário R$ '))
tempo = int(input('Digite em quantos anos deseja pagar? '))
mensal = tempo * 12
prestacao = casa / mensal

if prestacao <= salario * 0.3:
    print('Parabéns você foi aprovado!')
    print('A casa no Valor de R${:.2f}, terá a prestação de R${:.2f}' .format(casa, prestacao))
else:
    print('Prestação de R$ {:.2f} superior a 30% da Renda'.format(prestacao))
    print('Desculpa, financiamento não aprovado')
