#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo
n1 = int(input('Comprimento da primeira '))
n2 = int(input('Comprimento da segunda '))
n3 = int(input('Comprimento da terceira ')) 
if n1 + n2 > n3 and n2 + n3 > n1 and  n1 + n3 > n2:
    print('Pode formar')
else:
    print('Não pode formar')

