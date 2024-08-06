#Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informaçôes possiveis sobre ela
a = input("Digite qualquer coisa ")
print("O tipo primitivo do que vc digitou é ", type(a))   # =Qual o tipo primitivo da string
print("Só tem espaços?" , a.isspace())      # Tem espaço
print('É um numero?', a.isnumeric())        #A presença de numeros
print('É alfanumerico?', a.isalnum())       #Existe numeros e letras
print('Esta em maiusculo?', a.isupper())    #Esta em maiusculo
print('Esta em minusculo?', a.islower())    #Esta em minusculo
print('Esta capitaliada', a.istitle())      # Tem maiusculo e minusculo 

