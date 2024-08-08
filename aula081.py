#Crie um programa que vai ler varios numeros e coloca-los em uma lista
#depois disso mostre:
'''a) Quantos números fora digitados
b) A lista de valores de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista
'''
lista = []
for c in range(0,5):
    numero = int(input('Digite um número: '))  
    lista.append(numero)
    lista.sort(reverse=True)
print(f'Existem {len(lista)} números na lista. \n Sua ordem decrescente é ')
print(f'Sua ordem decrescente é {lista}')
if 5 in lista:
    print(f'O número 5 foi digitado na sua lista')
else:
    print(f'O número 5 não foi digitado')

    



