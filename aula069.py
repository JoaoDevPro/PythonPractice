#Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando um total de vitórias consecutivas que ele conquistou no final do jogo.#
from random import randint
cont = 0
while True:
    n = int(input("Vamos jogar impar ou par, escolha [1] IMPAR ou [2] para PAR: "))
    d = int(input("Digite um valor: "))
    pc = randint(1,10)
    v = (d + pc) 
    print('Um')
    print('dois')
    print('três')
    if n == 1: # impar
        if v % 2 != 0 :
            cont += 1
            print("Você venceu!")
            print("Jogador jogou {} e computador jogou {} Você venceu!".format(d, pc))
        else:
            print("Jogador jogou {} e computador jogou {} Você perdeu!".format(d, pc))
            break

    elif n == 2 :  #par
        if v % 2 == 0:
            cont += 1
            print("Jogador jogou {} e computador jogou {} Você venceu!".format(d, pc))
        else:
            print("Jogador jogou {} e computador jogou {} Você perdeu!".format(d, pc))
            break




   
print('Você ganhou {} vezes no impar ou par'.format(cont))
    

