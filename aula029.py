#Escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80 km/h. Mostre uma mensagem dizendo que ele foi multado
#A multa vai custar 7,00 por cada km acima do li
# mite
v = float(input('Diga a velocidade do seu carro '))
if v > 80:
    print('Sua munta é de {}'.format(7*(v-80)))
else:
    print('Você não vai ter multa')
