# A confederação nacional de natação precisa de um programa que leia a data de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: Mirin
# Até 14 anos: Infantil
#Até 19 anos: Junior
#Até 20 anos: Senior
#Master: Master
idade = int(input('Informe sua data de nascimento '))
if idade<= 9:
    print('Mirin')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <=19:
    print('Junior')
elif idade > 19 and idade <=20:
    print('Senior')
else:
    print('Master')