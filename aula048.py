#Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500
s = 0 
cont = 0
for c in range(0,501,2):
    if c % 3 == 0:
        cont = cont + 1
        s += c # A variavel recebe a variavel + c
print('Existem {} numeros multiplos de 3'.format(cont))
print('A soma dos mulplos de 3 é {}'.format(s))