#Crie um programa que leia uma frase pelo teclado e mostre :
#Quantas vezes aparece a letra 'a'
#Em que posição ela aparece a primeira vez 
#Em que posição ela aparece a ultima vez
palavra =str(input('Digite qualquer palavra ')).lower().strip #pra não contar os espaços
print(palavra.count('a'))
print(palavra.find('a')+1)# +1 pra ajeitar a posição
print(palavra.rfind('a')+1)

