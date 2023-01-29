peso = float(input('Qual o seu peso (Kg)?: '))
altura = float(input('Qual a sua altura (m)?: '))
imc = peso / (altura ** 2)
print('Seu imc é {:.2f} e sua classificação é '.format(imc), end="")
if imc < 18.5:
    print('só a titela!')
elif imc < 25:
    print('só o filé!')
elif imc < 30:
    print('só o ouro')
elif imc < 35:
    print('gordo')
elif imc < 40:
    print('gordão')
else:
    print('apto ao programa Kilos Mortais!')
#essas classificações são apenas uma brincadeira para deixar mais divertido minha aula!