#Melhore o jogo do desafio 28 onde o computado vai pensar em um número entre 0 e10. Só que agora o 
#computador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários 
#para vencer
import random
n = random.randint(0,5)
contador = 0
d = 1
while d != n:
    d =(int(input('Descubra o número que o pc escher bate com teu número, escolha um número de 1 a 5: ')))
    print('Você perdeu, tente novamente')
    contador = contador + 1
    if d > n :
        print('Menos... tente mais uma vez')
    else:
        print('Mais... Continue tentando!')
print('Vc venceuuu, vc usou {} pelpites para conseguir isso'.format(contador))


