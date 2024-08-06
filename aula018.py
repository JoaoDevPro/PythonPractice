#Faça um programa que leia um angulo qualquer e mostre  na sua tela o valor do seno, cosseno e tangente desse angulo, obs existe bibliotecas que pode fazer isso então é só pesquisar 
from math import radians, sin, cos, tan
a = int(input('Digite um angulo qualquer '))
num = sin(a) 
b = cos(a)
c = tan(a)
print('Seu seno é {:.2f}, seu cosseno {:.2f}, seu tangente {:.2f}'.format(num,b,c))