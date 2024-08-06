#Faça um programa que leia o comprimento do cateto oposto e cateto adjacente do triangulo retangulo. Calcule e mostre sua hipotenusa
n1 = float(input('Digite o valor do cateto oposto '))
n2 = float(input('Digite o valor do cateto adjacente '))
h = (n1 ** 2) + (n2 ** 2)
hip = h ** (1/2)
print('A hipotenusa referente aos dois catetos é {:.2f}'.format(hip))
# ou poderia ficar assim
# from math import hypot
#h = hypot (n1,n2)
#print('hypot')