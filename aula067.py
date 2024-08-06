#Crie um programa que leia varios números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada. No final, mostre quantos nímeros foram digitadose qual foi a soma entre eles, desconsiderando o flag#
cont = 0
n = 0
s = 0
while True:
    n = int(input('Digite um número :' ))
    if n == 999:
        break
    
    cont = cont + 1
    s = s + n
    
print('Vc digitou {} números e a soma entres eles foi de {}'.format(cont, s))
