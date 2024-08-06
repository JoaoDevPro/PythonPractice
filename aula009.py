# Faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada
n1 = int(input('Digite um nuemero para visualizar sua tabuada '))
for i in range(1, 11):
    print('{} x {} = {}'.format(n1,i,n1*i))


