print('{:=^40}'.format(' LOJAS MFRANKLIN '))
produto = float(input('Digite o valor do produto: R$'))
pagamento = int(input('Escolha a forma de pagamento: \n(1)À vista Dinheiro: \n(2)À vista no débito. \n(3)Em até 2x no cartão de crédito. \n(4)A partir de 3x no cartão de crédito. \nQual opção: '))
if pagamento == 1:
    produto = produto * 0.90
    print('O valor a ser pago: R${:.2f}'.format(produto))
elif pagamento == 2:
    produto = produto * 0.95
    print('O valor a ser pago: R${:.2f}'.format(produto))
elif pagamento == 3:
    parcelas = int(input('deseja em 1 ou 2 vezes: '))
    if parcelas == 1:
        print('O pagamento será em {} parcela no valor de R${:.2f}'.format(parcelas, produto))
    elif parcelas == 2:
        produto = produto / 2
        print('O pagamento será em {} parcelas no valor de R${:.2f}'.format(parcelas, produto))
elif pagamento == 4:
    parcelas = int(input('Qual o número de parcelas: '))
    if parcelas >= 3 and parcelas < 13:
        produto = (produto / parcelas) * 1.2
        print('O pagamento será em {} parcelas no valor de R${:.2f}'.format(parcelas, produto))
    else:
        print('Digite um número de parcelas válido!')
else:
    print('Digite uma opção válida!')
