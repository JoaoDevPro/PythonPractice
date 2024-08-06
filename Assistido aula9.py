frase = '  Trabaho na grey comercial  '
print(frase[3:13]) #Da quarta letra até o 12
frase = 'Trabaho na grey comercial'
print(frase[:13]) # Vai do inicio até a letra 12
frase = 'Trabaho na grey comercial'
print(frase[13:]) # Começa no 13 até o final da frase  
print(frase[3:13:2]) #Da quarta letra até o 12 pulando de 2 em 2
print(frase[3::2]) #Da quarta letra até o final pulando de 2 em 2
print(frase[::2]) #Do inicioda frase até o final pulando de 2 em 2
#Como dar um print em um texto gigante de uma só vez
#Exemplo de texto:
#Prezados, bom dia! Tudo bem?

#Sobre a questão de follow-up, os itens que vocês alegam estar em atraso já estão finalizados em nosso departamento de expedição, somente esperando a parte da coleta.

#IMPORTANTE: Realizamos apenas carregamentos em caminhões com carreta aberta devido o carregamento ser via ponte rolante.

#HORÁRIO DE FUNCIONAMENTO DA EXPEDIÇÃO:
#Segunda a Quinta-feira das 8:00 as 11:00 / 13:00 as 16:00hrs
#Sexta-feira das 8:00 as 11:00 / 13:00 as 15:00hrs;
print('''Prezados, bom dia! Tudo bem?

Sobre a questão de follow-up, os itens que vocês alegam estar em atraso já estão finalizados em nosso departamento de expedição, somente esperando a parte da coleta.

IMPORTANTE: Realizamos apenas carregamentos em caminhões com carreta aberta devido o carregamento ser via ponte rolante.

HORÁRIO DE FUNCIONAMENTO DA EXPEDIÇÃO:
Segunda a Quinta-feira das 8:00 as 11:00 / 13:00 as 16:00hrs
Sexta-feira das 8:00 as 11:00 / 13:00 as 15:00hrs;

''')
print(frase.count('a')) # Pra saber a quantidade de vezes que a letra 'a' aparece 
print(frase.upper()) # Passar todas as letras da frase pra maiúsculo 
print(len(frase)) # Pra saber o tamenho do texto contando os espaços
print(len(frase.strip())) # Pra saber o tamenho do texto sem os espaços
print(frase.replace('comercial', 'financeiro'))# Troca uma palatra por outra mas nãon salva 
print(frase)
frase = print(frase.replace('comercial', 'financeiro'))# Troca uma palatra por outra e agora salva 
#print('grey' in frase ) #mostra se a palavra está no texto ou não
# print(frase.find('grey')) mostra onde está localizada a frase 
#print(frase.lower().find('trabalho')) deixa tudo em minusculo
#print(frase.split()) cria uma lista das palavras com virgula e aspas 
#dividido = frase.split()
#print(dividido[0]) mostra a primeira palavra da lista 
#print(dividido[0] [3]) mostra a primeira palavra da lista e a primeira letra




