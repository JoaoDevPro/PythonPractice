# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade :
# Se ele ainda vai se alistar no serviço militar
# Se é hora de se alistar 
# Se ja passou do tempo de alistamento
# Seu programa deverá mostrar o tempo que falta ou que passou do prazo

from datetime import date
atual = date.today().year #Contabilizar os anos 
idade = int(input('Qual sua idade? '))
if idade < 18 :
    print('Faltam {} anos pra vc se alistar'.format(18 - idade))
    saldo = 18 - idade 
    ano = atual + saldo
    print('Você vai se alistar em {}'.format(ano))
elif idade == 18:
    print('Já está na hora do seu alistamento')
else :
    print('Você deveria ter se alistado a {} ano'.format(idade - 18))
    saldo = idade - 18
    ano = atual - saldo
    print('Vc deveria ter se alistado em {}'.format(ano))