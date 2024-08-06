#Desenvolva um programa que pergunte a distancia de uma viagem em km. calcule o preço da passagem cobrando 0,5 por km para viagens até 200km, e 0,45 para viagens mais longas 
d = float(input('Digite a distância da sua viagem '))
if d >= 200:
    print('O valor é de {}'.format(0,5 * d))
else :
    print('O valor é de {}'.format(0,45 * d))


