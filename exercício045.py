from random import randint
from time import sleep

nome = str(input('Qual seu nome jogador: '))
itens = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
pc = randint(0, 4)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
[ 3 ] Lagarto
[ 4 ] Spock
''')
jogador = int(input('Qual a sua jogada: '))
print('PEDRA')
sleep(0.5)
print('PAPEL')
sleep(0.4)
print('TESOURA')
sleep(0.3)
print('LAGARTO')
sleep(0.2)
print('SPOCK')
sleep(0.1)
print('=-_-' * 7)
print('Computador jogou {}!'.format(itens[pc]))
print('{} jogou {}!'.format(nome, itens[jogador]))
print('=-_-' * 7)
sleep(0.5)
if pc == 0: #PEDRA
    if jogador == 0:
        print('{} empata com {}' .format(itens[pc], itens[jogador]))
        print('EMPATOU')
    elif jogador == 1:
        print('{} é coberto por {}'.format(itens[pc], itens[jogador]))
        print('O jogador {} VENCEU!' .format(nome))
    elif jogador == 2:
        print('{} quebra a {}' .format(itens[pc], itens[jogador]))
        print('COMPUTADOR VENCEU!')
    elif jogador == 3:
        print('{} esmaga o {}' .format(itens[pc], itens[jogador]))
        print('COMPUTADOR VENCEU!')
    elif jogador == 4:
        print('{} quebra a {}' .format(itens[pc], itens[jogador]))
        print('O jogador {} VENCEU!' .format(nome))
elif pc == 1: #PAPEL
    if jogador == 0:
        print('{} cobre a {}' .format(itens[pc], itens[jogador]))
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('{} empata com {}'.format(itens[pc], itens[jogador]))
        print('EMPATOU')
    elif jogador == 2:
        print('{} é cortado pela {}' .format(itens[pc], itens[jogador]))
        print('O jogador {} VENCEU!' .format(nome))
    elif jogador == 3:
        print('{} é comido por {}' .format(itens[pc], itens[jogador]))
        print('O jogador {} VENCEU!' .format(nome))
    elif jogador == 4:
        print('{} refuta o {}' .format(itens[pc], itens[jogador]))
        print('COMPUTADOR VENCEU!')    
elif pc == 2: #TESOURA
    if jogador == 0:
        print('{} é quebrado por {}' .format(itens[pc], itens[jogador]))
        print('O jogador {} VENCEU!' .format(nome))
    elif jogador == 1:
        print('{} corta o {}'.format(itens[pc], itens[jogador]))
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('{} empata com {}' .format(itens[pc], itens[jogador]))
        print('EMPATOU')
    elif jogador == 3:
        print('{} decapita o {}' .format(itens[pc], itens[jogador]))
        print('COMPUTADOR VENCEU!')
    elif jogador == 4:
        print('{} é derretida por {}' .format(itens[pc], itens[jogador]))
        print('O jogador {} VENCEU!' .format(nome))   
elif pc == 3: #LAGARTO
    if jogador == 0:
        print('{} é esmagado por {}' .format(itens[pc], itens[jogador]))
        print('O jogador {} VENCEU!' .format(nome))
    elif jogador == 1:
        print('{} come o {}'.format(itens[pc], itens[jogador]))
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('{} é decapitado pela {}' .format(itens[pc], itens[jogador]))
        print('O jogador {} VENCEU!' .format(nome))
    elif jogador == 3:
        print('{} empata com {}' .format(itens[pc], itens[jogador]))
        print('EMPATOU')
    elif jogador == 4:
        print('{} envenena o {}' .format(itens[pc], itens[jogador]))
        print('COMPUTADOR VENCEU!')    
elif pc == 4: #SPOCK
    if jogador == 0:
        print('{} vaporiza a {}' .format(itens[pc], itens[jogador]))
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('{} é refutado por {}'.format(itens[pc], itens[jogador]))
        print('O jogador {} VENCEU!' .format(nome))
    elif jogador == 2:
        print('{} derrete a {}' .format(itens[pc], itens[jogador]))
        print('COMPUTADOR VENCEU!')  
    elif jogador == 3:
        print('{} é envenenado por {}' .format(itens[pc], itens[jogador]))
        print('O jogador {} VENCEU!' .format(nome))
    elif jogador == 4:
        print('{} empata com {}' .format(itens[pc], itens[jogador]))
        print('EMPATOU')
    else:
        print('Escolha uma opção válida!')