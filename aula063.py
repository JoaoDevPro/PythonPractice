#Escreva um programa que leia um numero n inteiro qualquer e mostre na telao n primeiros elementosde uma sequência de Fibonacci.

n1 = int(input('Até onde vc acha que vai a sequência Fibonacci: '))
t1 = 0
t2 = 1
print("{} -> {}".format(t1,t2), end="")
cont = 3
while cont != n1:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    cont += 1
    print(" -> {}".format(t3), end="")





