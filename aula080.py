# Crie um programa onde o usuário possa digitar 5 valores e cadastre em uma lista
# já na posição correta de inserção sem usar o sort(). No final, mostre a lista ordenada na tela
#explo ele le o 1 e depois o numero 4, quando voce digitar o numero 3, ele deverá ficar entre o 1 e 2 na lista pra ficar em ordem
lista = []
ordenado = []
for c in range(0, 5):
    num = int(input('Digite um número: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    else :
        pos = 0
        while pos < len(lista) :
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos+=1
        
    

print(f'Sua lista {lista}')
