from datetime import date

ano = date.today().year
nascimento = int(input('Digite o ano de nascimento:'))
idade = ano - nascimento
print('Atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação da categoria do atleta é MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação da categoria do atleta é INFANTIL')
elif idade > 14 and idade <20:
    print('Classificação da categoria do atleta é JÚNIOR')
elif idade <= 25:
    print('Classificação da categoria do atleta é SÊNIOR')
else:
    print('Classificação da categoria do atleta é MASTER')