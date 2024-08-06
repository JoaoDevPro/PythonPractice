#desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
#A media de idade do grupo
#Qual o nome do homem mais velho
#Homem mais velho
#Quantas mulheres tem menos de 20 anos 
somaidade = 0
maior = 0
menor = 0
maioridade = 0
maisvelho = ''
totmulher20 = 0
for p in range(1,6,+1):
    nome = str(input('Digite o {} nome '.format(p))).strip()
    idade = int(input('Digite a {} idade '.format(p)))
    sexo = str(input('Digite o {} genêro [M/F] '.format(p))).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridade = idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maioridade :
        maioridade = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 = totmulher20 + 1
    
media = somaidade/4
print('A média de idade do grupo é de {} anos.'.format(media))
print('O homem mais velho tem {} e se chama {}'.format(maioridade,maisvelho))
print('São {} melheres com menos de 21 anos'.format(totmulher20))



