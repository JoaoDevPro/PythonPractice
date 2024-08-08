#lista.append() pra adicionar um elemento no final da lista
#lista.insert(0, cachorroquente) Aqui eu adciono um cacho quente na minha lista e digo a qual posição ela vai ficar 
# del.lista(3) apagar na posição 3
# lista.pop(3) apagar na posição 3
#lista.remove(cachorroquente) apagar pelo nome do dado que você vai querer 
#lista.sort() para colocar os valores de maneira ordenada 1234
#listagem.sort(reverse=True) para colocar os valores de maneira inversa 4321
#len(lista) Para saber quantos elementos tem na minha lista 
#enumerate(lista) pra saber a posição de uma informação ou dado

'''lista = [2, 5, 4]
lista[2]= 3
lista.sort()
lista.append(7)
lista.insert(0, 9)
if 6 in lista:
    lista.remove(6)
print(f'{lista}')'''

'''
valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um número: ')))
valores.sort()
for c, n in enumerate(valores):
    print(f'Na posiução {c} enconrei o valor {n}...')
print('Cheguei ao final da lista')
'''
'''a = [2, 3, 4, 5]
b = a[:] # para criar uma cópia sem ter ligação
b[2]= 3
print(f'Lista {a}')
print(f'Lista {b}')'''



# Faça um programa que leia 5 valores numericos e guarde os em uma lista.
#No final, qual foi o maior e o menor digitado e as suas repectivas posições na lista
num = []
for c in range(0,5):
    num += [int(input('Digite um valor: '))] 
n1 = max(num)
n2 = min(num)

print(num)
print(f'O maior número é {n1} e tem aposição {num.index(n1) +1}')
print(f'O menor número foi o {n2} e sua posição foi o {num.index(n2) +1}')
