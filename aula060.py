#faça um programa que leia um número qualquer e mostre seu fatorial
#Ex; 5! = 5x4x3x2x1=120
from math import factorial

n = int(input('Digite um número pra ver seu fatorial: '))
c = n
f =1
print('Calculando {}! = '.format(n), end= '')
while c > 0:
    print(' {} '.format(c), end= '')
    print(' x ' if c > 1 else ' = ', end= '')
    f = f * c
    c = c-1
print( '{}'.format(f))
from math import factorial
'''n1 = int(input('Digite um número para o obter o calculo do seu fatorial: '))
for c in range(n1,0,-1):
    f = 1
    if c > 0:
        f = c * n1
        print('C')
        print(' {}! x'.format(c), end= '')'''



    
