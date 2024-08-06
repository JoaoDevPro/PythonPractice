# Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla
# Depois disso mostre a listagem de números gerados e também indique o menor e maior valor que está na tupa
import random
maior =0
menor = 0
a = random.randint(0,10)
b = random.randint(0,10)
c = random.randint(0,10)
d = random.randint(0,10)
e = random.randint(0,10)
v = 0
f = (a, b, c, d, e)
print(f)
for c in f:
    if maior == 0:
        maior = c
        menor = c
    if c >= maior:
        maior = c
    if menor > c:
        menor = c
print(f'O maior número é {maior} e o menor número é {menor}')
        
    
