#Crie um programa que leia dois valores e mostre um número na tela :
'''[1] soma
[2] multiplicador 
[3] maior
[4] novos numeros 
[5] sair do programa'''
# Seu programa devera realizar a operação realizada em cada caso
from time import sleep
q = 1
while q != 5 :
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    print('Escolha a operação que deseja realizar')
    print('[1] soma')
    print('[2] multiplicador')
    print('[3] maior')
    print('[4] novos numeros')
    print('[5] sair do programa')
    q = int(input('>>>>> Digite o número da operação que deseja realizar: '))
    if q == 1:
        soma = n1 + n2
        print('soma')
    if q == 2:
        multiplicador = n1 * n2
        print(multiplicador)
    if q == 3:
        if n1 > n2:
            print(n1, ' é o maior número')
        else:
            print(n2, ' é o maior número')
    if q == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    print('-=-' * 10)
    sleep(3)
print('FIM')
    


