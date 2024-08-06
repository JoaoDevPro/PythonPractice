#Desenvolva um programa que desenvolva números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar desconsidere-o
soma = 0
cont = 0
for c in range (1,7):
    n = int(input('Digite o {} numero : '.format(c)))
    if n % 2 == 0:
        cont = cont + 1
        soma = soma + n
print('Você informou {} números pares'.format(cont))
print('A soma dos numeros pares é {}'.format(soma))
