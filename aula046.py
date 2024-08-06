'''for c in range (1,6):
   print('oi')
print('fim')
for c in range (1,6):
    print(c)
print('fim')
for c in range (0,7,2): #Ele pula de 2 em 2
    print(c)
print('fim')
n =int(input('Digite um número: '))
for c in range (0,n):
    print(c)
print('Fim')
n = int(input('Inicio'))
n1 = int(input('Fim'))
n2 = int(input('Passo'))
for c in range (n,n1,n2):
    print(c)
print('Fim')
for c in range(0,3):
    n = int(input('Digite um valor')) # Quantas vezaes vai ser repetido a pergunta
print('Fim')
s = 0
for c in range (0,4):
    n = int(input('digite um valor: '))
    s += n # A variavel recebe a variavel + n
print('O somatório de todos os valores foi {}'.format(s))'''
# Faça um programa que mostre na tela uma contagem regressiva para um estoura de fotos de artificios,
#inicio de 10 até 0, com uma pausa de um segundo entre elas.
from time import sleep
for c in range(10,0,-1):
    print(c)
    sleep(1)
print('POOOW')

