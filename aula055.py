#faça um programa que leia o peso de 5 pessoas. No final, mostre o maior e o menor peso lidos
maior = 0
menor = 99999

for p in range(1,6,+1):
    peso =float(input('Informe o peso da {} pessoa : '.format(p)))
    if peso > maior:
        maior = peso
    elif peso < menor:
         menor = peso
print(maior)  
print(menor)

       
