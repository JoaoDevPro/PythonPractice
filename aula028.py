# Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O usuário deverá escrever na tela se o usuário venceu ou perdeu
import random
n = random.randint(0,5)
d =(int(input('Descubra o número que o pc escher bate com teu número, escolha um número de 1 a 5 ')))
if n == d:
    print('Você venceu ')
else :
    print('Você perdeu ')
