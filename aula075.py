#Desenvolva um programa que leia 4 valores pelo teclado e guade - os em um tupla
# quantas vezes apareceu o valor 9
# Em que posição foi digitado o valor valor 3
# Quais foram os números pares
cont = 0
par = 0
a = 0
b = 0
d = 0
e = 0
f = 0
for c in range(0, 4):
    c = int(input("Digite um número:"))
    cont += 1
    if c % 2 == 0:
        par = (c)
    if cont == 1:
        a = c
    if cont == 2:
        b = c
    if cont == 3:
        d = c
    if cont == 4:
        e = c
    if cont == 5:
        f = c

tupla = (a, b, d, e, f)


print(tupla.count(9))
print(tupla.index(9))
print(f'O número {par} é par')
