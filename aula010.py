# Crie um programa que leia todo dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar ( Considere 1 dolar = 3,27)
d = float(input('Digite o valor que você tem '))
cont = d / 3.27
print('Seu valor em dólar é de {:.2f}'.format(cont))