# Refaça o desafio 035 dos triângulos, acrescentando o recurso mostrar que tipo de triângulo será informado:
# Equilátero: todos os lados iguais
# Isóceles: dois lados iguais 
# Escaleno: Todos os lados diferentes 
#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo
n1 = int(input('Comprimento da primeira '))
n2 = int(input('Comprimento da segunda '))
n3 = int(input('Comprimento da terceira ')) 
if n1 + n2 > n3 and n2 + n3 > n1 and  n1 + n3 > n2:
    print('Pode formar')
    if n1 ==n2 and n2 == n3 and n1 == n3:
        print('O triangulo é Equilátero') 
    elif n1 != n2 and n1 != n3:
        print('O triangulo é escaleno')
    else:
        print('O triangulo é isóceles')
else:
    print('Não pode formar')