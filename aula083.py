'''
crie um programa onde o usuario digite uma expressão qualquer que use parenteses.
Seu aplicativo deverá analisar se a expressão passada esta com os pareenteses abertos ou fechados na ordem correta
'''
lista = []
f = input('Digite sua função aqui: ')
cont = 0
conts = 0
for c in f:
    if c == "(" or c == ")":
        cont += 1 
if cont % 2 == 0:
    print(f'Sua função está com o fechamento certo')
else:
    print(f'Sua função está com o fechamento errado')
    '''if  c == ")":
        conts += 1 
        if conts % 2 == 0:
            print(f'Sua função está com o fechamento errado')
        else:
            print(f'Sua função está com o fechamento certo')'''
        