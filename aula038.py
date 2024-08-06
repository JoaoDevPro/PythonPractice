# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior 
# O segundo valor é maior 
# Não existe valor maior, os dois são iguais 
n = int(input("informe o primeiro número "))
d = int(input("informe o segundo número "))
if n>d :
    print(n ,'É o maior')
elif d>n :
    print(d ,'É o maior')
else:
   print('Eles são iguais') 