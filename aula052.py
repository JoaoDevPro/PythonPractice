#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo 

    

a = int(input('Digite um número pra saber se ele é primo: '))
tot = 0
for c in range (1,a + 1, +1):
    if a % c == 0 or a % c == a :
         tot += 1
if tot == 2 :
    print('O {} é um número primo'.format(a))
else:
    print('O {} não é um número primo'.format(a))
       
       