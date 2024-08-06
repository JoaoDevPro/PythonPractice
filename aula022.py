#Crie um programa que leia um nome completo de uma pessoa e mostre:
# O nome com todas as letras maiuscula
# o nome com todas minusculas
#todas as letras ao todo sem considerar espaços 
# quantas letras tem o primeiro nome 
nome = str(input('digite seu nome completo '))
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(nome.find(' '))
separa = nome.split()
print(separa[0], len(separa[0]))
