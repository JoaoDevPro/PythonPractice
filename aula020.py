# o mesmo professor do desafio anterior quer sortear a ordem de apresentação,de trabalho dos alunos,. Faça um programa que leia o nome dos quatro anunos e mostre a ordem sorteada . De cinco alunos ele quer sortear e saber quem vai apresentar primeiro, segundo...
from random import shuffle
n1 = str(input('Digite o nome do primeiro anulo '))
n2 = str(input('Digite o nome do segundo anulo '))
n3 = str(input('Digite o nome do terceiro anulo '))
n4 = str(input('Digite o nome do  quarto anulo '))
n5 = str(input('Digite o nome do  quinto anulo '))
lista = [n1,n2,n3,n4,n5]
shuffle(lista)
print('Os alunos sorteados são {}'.format(lista))
