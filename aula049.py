#refaça o desafio 009, mostrando a tabuada de um número que a pessoa escolher, só que agora ultilizando um laço for
n = int(input('Insira o número da tabuada desejada : '))
for c in range (1,11):
    print('{} x {} = {}'.format(n,c,n*c))
