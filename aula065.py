#Crie um programa que leia varios números inteiros pelo teclado. No final da execução mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
n = 0
cont = a = soma =  maior= menor= 0
a = int(input("Diga um numero "))
while n != "n":
    cont += 1
    soma +=  a
    a = int(input("Diga um numero "))
    if cont == 1:
         maior = a
         maior = menor = a
    else:
        if  a > maior :
            maior = a
        if  a < menor:
            menor = a
            
    n = str(input("Quer continuar [n/s]"))
media = soma / cont
print("A media de todos os números foram {}, o maior é {} e o menor é {}".format(media, maior, menor))
print("Acabou")
