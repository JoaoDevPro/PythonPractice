#Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
a = int(input("Digite 1 se quiser ver termos e coloque 0 para sair"))
while a == 1:
    cont = 0
    soma = 0
    while cont != 2:
        a = int(input('Insira o termo: '))
        b = int(input('Insira a razão da PA: '))
        decimo = a + soma +(10-1) * b
        for c in range(a,decimo + b,b):
            print('{}'.format(c), end='->')
    a = int(input("Termos vc ainda quer? "))
print("Fim")
    
    
    
