#Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros 
n1 = float(input('Digite o valor em metros que voce quer converter '))
cent = n1 *100
mili = n1 * 1000
print('Seu valor convertido em centimetros é {:.2f} , e em milimetros {:.2f}'.format(cent,mili))
# :.2f dentro do {} no print indica duas casas decimais depois da virgurla 