#Crie um programa que leia varios numeros inteiros pelo nteclado.O programa só vai parar quando o usuário digitar o valor 999, 
#que é a condição da parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

cont = 0
a = 0
soma = 0
a = int(input("Diga um numero "))
while a !=999: 
    cont += 1
    soma +=  a
    a = int(input("Diga um numero "))
dif = soma - 999
print("Vc digitou {} e a soma de todos os números foram {}".format(cont,soma))
print("Acabou")
