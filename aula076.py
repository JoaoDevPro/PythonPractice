# Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços na sequencia
#No final mostre uma listagem de preços, organizando os dados de forma tubular
'''produto1 =(12 ," Sabão em pó")
produto2 = (13 ," Amaciante ")
produto3 = (14 ," Álcool ")
produtos = (produto1, produto2, produto3)
maior = 0

if produto1[0] > produto2[0] and produto1[0] > produto3[0]:
        print(produto1)
        if produto2[0] > produto3[0]:
            print(produto2)
            print(produto3)
        else :
            print(produto3)
            print(produto2)
            
        
if produto2[0] > produto1[0] and produto2[0] > produto3[0]:
        print(produto2)
        if produto1[0] > produto3[0]:
            print(produto1)
            print(produto3)
        else :
            print(produto3)
            print(produto1)

if produto3[0] > produto1[0] and produto3[0] > produto2[0]:
        print(produto3)
        if produto1[0] > produto2[0]:
            print(produto1)
            print(produto2)
        else :
            print(produto2)
            print(produto1)'''

listagem= (
    "lapiz", 1.75,
    "caneta", 2.00,
    "shampoo", 10,
    "sabonete", 2.75
        )
print("-"*20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30} R$', end='')
    else:
        print(f'{listagem[pos]:>7.2f}')