'''c = 1
while c < 10:
    print(c)
    c = c + 1
print('fim')'''
'''n = 1
while n != 0:
    n = int(input('valor: '))
print('fim')'''
r = 's'
'''while r == 's':
    n = int(input('valor: '))
    r = str(input('Quer continuar?')).lower()
print('fim')'''
'''n = 1
par = impar = 0
while n != 0:
    n = int(input('valor '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('O numeros par é igual a {} e o numeros impares é igual a {}'.format(par, impar))'''
#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores m ou f. caso esteja errado faça a digitação novamente até ter um valor correto


sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Escolha [M/F] para identificar seu gênero ')).upper()
print('Fim')