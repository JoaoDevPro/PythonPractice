#Desenvolva um programa que leia 4 valores pelo teclado e guade - os em um tupla
# quantas vezes apareceu o valor 9
# Em que posição foi digitado o valor valor 3
# Quais foram os números pares
vetor = []
par = 0
for c in range(0, 4):
    num = int(input("Digite um número:"))
    vetor.append(num)
    if num % 2 == 0:
        par += 1

print(vetor)
print(f'O numero 9 apareceu {vetor.count(9)} vezes')
print(f'Ao todo, tivemos {par} números par')
if 3 in vetor:
    print(f'A posição é {vetor.index(3) + 1}')
else:
    print('Valor 3 não informado')

   





