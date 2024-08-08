'''
Crie um programa que leia varios numeros e colocar em uma lista
depois disso crie duas listas extras que vão conter apenas os valores paraes e os valores impares
digitados,
respectivamente

Ao final mostre o conteúdo das 3 listas geradas
'''
lista = []
p = 0

while p != 'n':
    par = [] # Importante definir as variaveis antes do loop
    impar = []
    n = int(input('Digite um número: '))
    lista.append(n)
    for c in lista:
        if c % 2 == 0:
            par.append(c)
        else:
            impar.append(c)

    p = str(input('Quer continuar? '))

print(f'{lista}')
print(f'Os números pares são {par}')
print(f'Os números impares são {impar}')


