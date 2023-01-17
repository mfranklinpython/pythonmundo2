from datetime import date

nascimento = int(input('Digite o ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - nascimento 
if idade < 18:
    falta = 18 - idade
    print('Sua idade é {} falta {} anos para seu alistamento.' .format(idade, falta))
    ano = anoAtual + falta
    print('Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    falta = idade - 18
    print('Sua idade é {} seu alistamento foi há {} anos.'.format(idade, falta))
    ano = anoAtual - falta
    print('Seu alistamento foi em {}.'.format(ano))
else:
    print('Você tem {} procure a junta militar mais próxima!'.format(idade))
