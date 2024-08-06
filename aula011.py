#Faça um programa que leia a largura e altura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo que casa litro de tinta, pinta uma area de 2 metros quadrados 
l = float(input('informe largura '))
a = float(input('informe altura '))
quant = (l * a) / 2
print('A quantidae de latas de tinta vai ser {}'.format(quant))
