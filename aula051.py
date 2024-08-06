#desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão
a = int(input('Insira o termo: '))
b = int(input('Insira a razão da PA: '))
decimo = a + (10-1) * b
for c in range(a,decimo + b,b):
    print('{}'.format(c), end='->')
print('Fim')