# Desenvolva a lógica que leia o peso e altura de uma pessoa, calcule seu imc e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5 : Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: obesidade
# Acima de 40 : Obesidade mórbida 
altura = float(input('Informe sua altura '))
peso = float(input('Informe sua peso '))
imc = peso / (altura ** 2)
print('O imc é de {}'.format(imc))
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('peso ideal')
elif imc >= 25 and imc <30 :
    print('sobrepeso')
elif imc >=30 and imc < 40:
    print('Obesidade')
else :
    print('Obesidade mórbida')

