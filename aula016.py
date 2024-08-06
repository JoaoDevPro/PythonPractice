#Buscando raiz na biblioteca aplicando na variável math.sqr(num)
import math
num = int(input('Digite um número para ver sua raiz quadrada '))
raiz = math.sqrt(num)
print('Sua raiz é {}'.format(raiz))
#Arredondando o resultado pra cima usando ceil
import math
num = int(input('Digite um número para ver sua raiz quadrada '))
raiz = math.sqrt(num)
print('Sua raiz é {}'.format(math.ceil(raiz)))

# Uma maneira de não precisar ficar colocando math toda hora é colocar uma vez e dizer as funções que você quer que ele puxe do lado
#import math sqrt, floor
#num = int(input('Digite um número para ver sua raiz quadrada '))
#raiz = sqrt(num)
#Pra você gerar um número aleátório 
import random
num = random.random()
print(num)
#Pra você gerar um número aleátório inteiro de um parâmetro até outro
import random
num = random.randint(1,10)
print(num)
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex 3.343 = 3
import math 
n = float(input('Digite um número qualquer '))
print('Sua porção inteira é{}'.format(math.trunc(n)))

