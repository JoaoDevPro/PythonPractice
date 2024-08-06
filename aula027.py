#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e ultimo nome separadamente
#ex: Ana maria de solza
#primeiro = ana 
#ultimo = solza 
nome = str(input('Diga teu nome ')).strip()
dividido = nome.split()
print(dividido[0])
print(dividido[len(dividido)-1]) # o -1 pra mostrar o ultimo nome nome que iria ser retirado
