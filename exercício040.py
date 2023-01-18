nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
mediaAluno = (nota1 + nota2) / 2
if mediaAluno < 5:
    print('Com a média {:.1f} e {:.1f}.'.format(nota1, nota2))
    print('Sua média foi {:.1f}. O aluno está REPROVADO'.format(mediaAluno))
elif mediaAluno >= 5 and mediaAluno < 7:
    print('Com a média {:.1f} e {:.1f}.'.format(nota1, nota2))
    print('Sua média foi {:.1f}. O aluno está de RECUPERAÇÃO'.format(mediaAluno))
else:
    print('Com a média {:.1f} e {:.1f}.'.format(nota1, nota2))    
    print('Sua média foi {:.1f}. Parabéns você foi APROVADO'.format(mediaAluno))