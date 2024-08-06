# Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa. O programa Vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exeder 30% do salário ou então o emprestimo será negado
casa = float(input("Informe o valor da casa que vc quer comprar "))
salario = float(input("Informe seu salário "))
tempo = float(input("Em quantos anos vc vai pagar ? "))
valor = (casa/tempo)/12
porcentagem = (salario*30)/100
if valor < porcentagem :
    print("Seu emprestimo foi aceito")
else:
    print("Seu emprestimo foi negado")