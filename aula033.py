#faça um programa que leia três numeros e mostre qual é o maior e o menor 
n1 = int(input('Digite um número '))
n2 = int(input('Digite outro '))
n3 = int(input('Digite mais um '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3 :
    maior = n2
if n3> n1 and n3 > n2:
    maior = n3

print('O maior é {} e o menor é {}'.format(maior, menor))
