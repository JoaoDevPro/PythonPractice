#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo".
cidade =str(input('Diga o nome de uma cidade ')).strip()
print(cidade[:5].lower() == 'santo')