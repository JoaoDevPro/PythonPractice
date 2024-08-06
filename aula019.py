#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude eles lendo o nome deles e escrevendo o nome do escolhido.  obs biblioteca
import random
n1 = str(input('Digite o nome do primeiro anulo '))
n2 = str(input('Digite o nome do segundo anulo '))
n3 = str(input('Digite o nome do terceiro anulo '))
n4 = str(input('Digite o nome do  quarto anulo '))
n5 = str(input('Digite o nome do  quinto anulo '))
lista = [n1,n2,n3,n4,n5]
escolhido = random.choice(lista)
print('O aluno sorteado é {}'.format(escolhido))
# ou poderia ficar assim 
from random import choice 
n1 = str(input('Digite o nome do primeiro anulo '))
n2 = str(input('Digite o nome do segundo anulo '))
n3 = str(input('Digite o nome do terceiro anulo '))
n4 = str(input('Digite o nome do quarto anulo '))
n5 = str(input('Digite o nome do quinto anulo '))
lista = [n1,n2,n3,n4,n5]
escolhido = choice(lista)
print('O aluno sorteado é {}'.format(escolhido))
