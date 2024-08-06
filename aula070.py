#Crie um programa que leia a idade e sexo de varias pessoas. A cada pessoas cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre
# A Quantas pessoas tem mais de 18 anos
# B Quantos homens foram cadastrado
# C Quantas mulheres tem menos de 20 anos
#

cont = 0
cont2 = 0
cont3 =0
cont4 = 0
menor = 0
while True:
    a = int(input("Digite [1] para cadastrar uma nova pessoa e [2] para sair "))
    if a == 2:
        break
    sexo = int(input("Diga o seu sexo, 1 [h] e 2 para [m] "))
    if sexo == 1:
        idade_m = int(input("Diga a idade da pessoa que quer cadastrar "))

        if idade_m > 18:
            cont3 += 1
        if idade_m > 18:
            cont += 1 
    elif sexo == 2:
        idade_f = int(input("Diga a idade da pessoa que quer cadastrar "))
        if idade_f < 20:
            cont2 += 1
        if idade_f > 18:
            cont4 += 1

    
    
    
    
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    
    
    
    

    
   
print('Tem {} pessoas mais de 18 anos,  {} homens foram cadastrados,  e {} mulheres com menos de 20 anos '.format(cont + cont4 ,cont3,cont2))
        
        

