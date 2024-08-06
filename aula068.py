# Faça um programa que leia a tabuada de vários números, um de cada vez para o valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo
e = 0
n = 0
r = 0
while True:
    t = int(input('Digite um número para a sua tabuada '))
    print('-=' * 30)
    if t < 0 :
        print("Valor incorreto, operação encerrada ")
        break
    for c in range(1,11):
        print('{} X {} = {}'.format(t, c, t * c))
    print('-=' * 30)

    

    
     


