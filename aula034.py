#Escreva um programa que pergunte o salário de um funcionário e pergunte o valor de seu almento.
#Para salários maiores de 1250,00 calcule um aumento de 10%, para inferios ou iguais o aumento é de 15%
s = float(input('Diga seu salário '))
aumento1 = (15 * s)/ 100
aumento2 = (10 * s)/100
if s <= 1250:
    print('Seu aumento é de {}'.format(aumento1 + s))
else:
    print('Seu aumento é de {}'.format(aumento2 + s))
