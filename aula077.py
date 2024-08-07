# Crie um programa que tenha uma tupla com varias palavras(n usar acentos)
#depois disso vc deve mostrar para cada palavra, quais são as suas vogais
palavras = ("ritimia", "doce", "pirulito", "bala", "algodao", "mostarda" )
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

