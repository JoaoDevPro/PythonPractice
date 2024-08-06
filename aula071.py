#Crie um programa que leia o nome e o preço de varios produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
#Qual é o total gasto na compra    Quantos produtos custam mais de 1000 reais   Qual o nome do produto mais barato
total = 0
cont = 0
menor = 0
contador = 0
baratp = ''
while True:
    a = int(input('Clique [1] para a leitura de um novo produto e [2] para sair: '))
    if a == 2:
        break
    b = str(input('Diga o nome do produto : '))
    c = int(input('Qual o valor do produto : '))
    total += c
    contador += 1
    if contador == 1:
        menor = c
        barato = b
    else:
        if c < menor:
            menor = c
            barato = b

    if c >= 1000:
        cont += 1
    
    
    
    
    

    print('=-=-=' * 30)

print('O gato total da compta foi {}. Teve {} que custaram mais de 1000 reais. E o produto mais barato foi o {}'.format(total, cont, barato))

    
    

