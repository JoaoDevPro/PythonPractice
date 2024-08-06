# Faça um programa que faça o computador jogar jokenpô com você.
from random import randint 
from time import sleep
print('Vamos jogar jokenpo ?')
itens = ('Pedra', 'Papel', 'Tesoura')
lista = randint(0,2)
print('''Suas opções
        [0] Pedra
        [1] Papel  
        [2] Tesoura''')
n = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('POO')
sleep(1)
print('-=' * 11)
print('Computador jogou {}'.format(itens[lista]))
print('Jogador jogou {}'.format(itens[n]))
print('-=' * 11)
if lista == 0:
    if n ==0:
        print('Empate')
    elif n == 1:
        print('venceu')
    elif n == 2:
        print('perdeu')
    else:
        print('jogada invalida')
elif lista == 1:
    if n ==0:
        print('Perdeu')
    elif n == 1:
        print('Empate')
    elif n == 2:
        print('venceu')
    else:
        print('jogada invalida')
elif lista == 2:
    if n ==0:
        print('Venceu')
    elif n == 1:
        print('Perdeu')
    elif n == 2:
        print('Empate')
    else:
        print('jogada invalida')

