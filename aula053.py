#Crie um programa que leia uma frase qualquer e diga se ele é um polindromo, desconsidere os espaços
frase = str(input('Digite uma frase para ver se ela um polindromo: ')).strip().upper() #tira os espaços e já joga pra maiusculo
palavras = frase.split() # separa em palavras 
junto = ''.join(palavras) # junta tudo
inverso =''
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
    print(junto,inverso)'''
if inverso == junto:
    print(frase,inverso)
    print('ele é um palindromo')
else:
    print('ele não é um palindromo')