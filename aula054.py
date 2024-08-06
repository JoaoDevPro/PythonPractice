#Crie um programa que leia a data de nascimento de 7 pessoas . No final mostre quantas pesssoas ainda não atingiram a maioridade e quantas já são de maiores
from  datetime import date
atual = date.today().year
contm = 0
cont = 0
for c in range(1,4):
    data =int(input('Em que ano a {} nasceu? '.format(c)))  #39
    anos = atual - data
    print('A {} pessoa tem {} anos'.format(c,anos))
    if anos >= 18:
        contm += 1
    else:
        cont += 1
print('Tem {} pessoas maior de idade'.format(contm))
print('Tem {} pessoas maior de idade'.format(cont))
