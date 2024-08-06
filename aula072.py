#Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual o valor a ser sacado (número inteiro) e o programa vai informar quantas cedulas de cada valor serão entregues
#obs Considere que o caixa possui cedulas de $50  $20  $10 e $1

"""valor = int(input('Olá, qual o valor que deseja sacar? '))
ced = 50
total = valor
totced = 0

while True:
    if valor >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
    if total == 0:
        break
print('Volte sempre')"""
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensão, de zero até 20. Seu programa deverá ler seu número pelo teclado(entre 0 e 20) e mostralo por extenso
tupla =("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")
numero = int(input("Digite um número de 0 a 20 para vê-lo por extenso: "))
print(tupla[numero])





